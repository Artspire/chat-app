# Project 2

<b>Web Programming with Python and JavaScript</b>

For project2, I have made, per the requirements, an online messaging service called Flack. This project makes use of the <a href="https://flask-socketio.readthedocs.io/">Flask-SocketIO</a> library and the <a href="https://socket.io/">SocketIO</a> JavaScript library.

## Layout

The design of the website is fairly minimalist with a combination of fairly bright colors. I have made use of Bootstrap for the layout, including the grid system and a navbar. The size of the containers change depending on the width of the screen, making the website responsive and look good on all screen sizes.

## Files

My project folder includes a <i>static</i> folder containing an image for the `error.html` page, an icon and a `styles.css` file. The <i>templates</i> folder contains 5 .html template files that make up the website. The SocketIO JavaScript code can all be found at the bottom of the `layout.html` file. Furthermore, the project folder contains a `requirements.txt` file listing all the Python packages used, a `helpers.py` file that defines the @login-required function and, lastly, an `application.py` file that contains all the necessary Flask code for running the website.

## Functionality


### Personal touch

My personal touch is the ability to change the display name on the channel page, which turned out to be quite challenging. At first, I was trying ...

to via a form that gets posted (which reloads the page) with emitting a message to all users that a user has changed his/her display name.

Extracting the new display name form the message that gets emitted and updating the `session['username']` variable that way.
# project2
