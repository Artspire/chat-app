import os

from flask import Flask, redirect, render_template, url_for, request, session
from flask_session import Session
from flask_socketio import SocketIO, emit, join_room, leave_room
from datetime import datetime

from helpers import login_required

app = Flask(__name__)
app.config["SECRET_KEY"] = 'mysecret'
socketio = SocketIO(app)

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

channels = []
chat_history = {}


@app.route("/" , methods=["GET", "POST"])
@login_required
def index():

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # If user creates a channel
        if request.form.get("channel"):
            channel = request.form.get("channel")

            # Show error page if channel already in list
            if channel in channels:
                return render_template("error.html", message="channel already exists")

            # Add channel if not yet in list
            if channel not in channels:
                channels.append(channel)

                # Creat empty list for channel in chat_history dictionary
                chat_history[channel] = []

        return redirect(url_for('channel', channel_id=channel))

    # User reached route via GET (as by clicking a link or via redirect)
    else:

        # If the user has previously chatted in a channel
        if "last_channel" in session:
            last_channel = session['last_channel']

            # Redirect user to the last channel user was on
            if last_channel in channels:
                return redirect(url_for('channel', channel_id=last_channel))

        return render_template("index.html", channels=channels)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return render_template("error.html", message="please provide a display name")

        # Store username in session variable
        session['username'] = request.form.get("username")

        # Also store username in session variable 'oldusername'
        session['oldusername'] = session['username']

        # Redirect user to main page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/channel/<string:channel_id>", methods=["GET", "POST"])
@login_required
def channel(channel_id):
    """Channel page"""

    # Get name of channel
    id = channel_id

    # Store the last channel the user visited in session variable
    session['last_channel'] = channel_id

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # If user changes display name, clear and update session variable
        ## Form submission disabled in JavaScript
        if request.form.get("username"):
            session['oldusername'] = session['username']
            session.pop('username', None)
            session['username'] = request.form.get("username")

        # If user creates a channel
        if request.form.get("channel"):
            channel = request.form.get("channel")

            # Show error page if channel already in list
            if channel in channels:
                return render_template("error.html", message="channel already exists")

            # Add channel if not yet in list
            if channel not in channels:
                channels.append(channel)

                # Creat empty list for channel in chat_history dictionary
                chat_history[channel] = []

        return render_template("channel.html", id=id, messages=chat_history[channel_id], channels=channels)

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("channel.html", id=id, messages=chat_history[channel_id], channels=channels)


@socketio.on("join_channel")
def on_join(join):
    join_room(join)


@socketio.on("submit message")
def messages(data):

    message = data["message"]
    room = data["channel"]

    join_room(room)

    # Get timestamp
    now = datetime.now()
    timestamp = now.strftime("%H:%M:%S")

    if message == 'has connected':
        entire_message = session['username'] + " " + message

    else:
        entire_message = session['username'] + ": " + message + " " + "[" + timestamp + "]"

        # Delete first message if total messages stored in list reaches maximum of 100
        if len(chat_history[room]) == 100:
            del chat_history[room][0]

        # Store message into messages dictionary
        chat_history[room].append(entire_message)

    print(entire_message)

    emit("announce message", entire_message, room=room)


@socketio.on("change name")
def change(data):

    username = data["username"]
    room = data["channel"]

    join_room(room)

    # If user changes display name, clear and update session variable
    session.pop('username', None)
    session['username'] = username

    entire_message = session['oldusername'] + " has changed his/her name to " + username

    # Update 'oldusername' session variable to the new display name
    session['oldusername'] = session['username']

    emit("announce message", entire_message, room=room)


@socketio.on("leave_channel")
def on_leave(leave):

    # Remove the last channel from session variable
    session.pop('last_channel', None)
    leave_room(leave)


if __name__ == '__main__':
    socketio.run(app)
