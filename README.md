# Project 2

<b>Web Programming with Python and JavaScript</b>

For project2, I have made, per the requirements, an online messaging service called Flack. This project makes use of the <a href="https://flask-socketio.readthedocs.io/">Flask-SocketIO</a> library and the <a href="https://socket.io/">SocketIO</a> JavaScript library.

## Layout

The design of the website is quite minimalist with a combination of fairly bright colors. I have made use of Bootstrap for the layout, including the grid system and a navbar. The size of the containers change depending on the width of the screen, making the website responsive and look good on all screen sizes.

## Files

My project folder includes a <i>static</i> folder containing an image for the `error.html` page, an icon and a `styles.css` file. The <i>templates</i> folder contains 5 .html template files that make up the website. The SocketIO JavaScript code can all be found at the bottom of the `layout.html` file. Furthermore, the project folder contains a `requirements.txt` file listing all the Python packages used, a `helpers.py` file that defines the @login-required function and, lastly, an `application.py` file that contains all the necessary Flask code for running the website.

## Functionality

When a user browses to Flack for the first time, the user is asked to enter a display name. After registration, the user is taken to the homepage where he or she can create a channel or select one of the existing channels. If the user decides to create a new channel, the user is automatically redirected to the channel after clicking the "create channel" button. If the channel already exists, however, the user will be shown an error.

On the channel page, the user will be presented with all the messages - with a maximum of 100 - that have previously been sent in the channel by other users. If the channel was just created by the user, there will naturally be no previous messages to display.

When the users decides to type a message and clicks on the "send message" button, the message will then be shown to all the users in that channel including the display name of the user and the time the message was sent by the user.

The user can also change his/her display name on the channel page. See the last paragraph below for more information regarding this functionality.

Lastly, if the user closes the browser tab of a channel page and later re-opens Flack, the user will automatically be redirected to the last channel the user was chatting in.

### Personal touch

My personal touch is the ability to change the display name on the channel page, which turned out to be quite challenging. At first, I was trying to combine changing the display name via a form that sends the user data to the current page with emitting a message to all users that a user has changed his/her display name. This does not work, however, because the form submission reloads the page.

Disabled the form. in JavaScript.

Extracting the new display name from the message that gets emitted and updating the `session['username']` variable that way.

The `session['oldusername']` variable - which is also set on the login page - is updated after `entire_message`

When a user changes his/her display name on the channel page, all users in the channel get a notification that specifies who changed their display name and also what the new display name of that user is.

The only ... , however, is that it only works for as long as the user stays in the channel. Leaving the channel, reloading the page or closing the browser tab all result in the display name being reset to the old display name.

While this arguably makes the functionality more interesting, I cannot entirely explain why this happens.
