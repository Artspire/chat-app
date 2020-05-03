$(document).ready(function() {

  // Connect to websocket
  var socket = io.connect(location.protocol + '//' + document.domain + ':' + location.port);

  socket.on('connect', function() {
    socket.send('User has connected');
  });

  socket.on('message', function(text) {
    $("#messages").append('<li>' + text + '</li>');
  });

  $('#send-button').on('click', function() {
    socket.send($('#message-input').val());
    $('#message-input').val('');
  });
});
