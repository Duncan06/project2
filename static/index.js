document.addEventListener('DOMContentLoaded', () => {
  var socket = io.connect(location.protocol + '//' + document.domain + ':' + location.port);

  socket.on('connect', () => {
    document.querySelector('.form-container').onsubmit = () => {
      const message = document.querySelector('#message').value;
      socket.emit('message', {'userschat': message});
    };
  });

  socket.on('chat', data => {
    const post = document.createElement('div');
    post.clasName= 'container';
    post.innerHTML= `${data.message}`;
    document.querySelector('.form-container-chat').append(post);
  });
});
