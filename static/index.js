document.addEventListener('DOMContentLoaded', () => {
  var socket = io.connect(location.protocol + '//' + document.domain + ':' + location.port);

  socket.on('connect', () => {
    document.querySelector('.form-container').onsubmit = () => {
      const message = document.querySelector('#message').value;
      console.log('message made');
      socket.emit('message', {'message': message});
    };
  });

  socket.on('chat', data => {
    const post = document.createElement('div');
    post.className = 'container';
    post.innerHTML = `${data.user}`;
    console.log('message sent');
    document.querySelector('.form-container-chat').append(post);
    socket.emit('post', {'post': post});
  });
});
