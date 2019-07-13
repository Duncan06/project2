document.addEventListener('DOMContentLoaded', () => {
  var socket = io.connect(location.protocol + '//' + document.domain + ':' + location.port);

  socket.on('connect', () => {
    socket.emit('message', {'userschat': userschat});
  });

  socket.on('chat', data => {
    const li = document.createElement('li');
    li.innerHTML = `Message sent: ${data.selection}`
    document.querySelector(#messages).append(li)
  })
});
