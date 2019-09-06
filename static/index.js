document.addEventListener('DOMContentLoaded', () => {

  const request = new XMLHttpRequest();
  request.open('POST', '/chat')
  request.onload = () => {
    const data = JSON.parse(request.responseText);
    localStorage.setItem("chatid", data["chatid"])
    let a;
    for (a=0; a<data["chat"]["message"].length; a++) {
      const message = data["chat"]["message"][a]
      post.className = 'container'
      post.innerHTML = message;
      document.querySelector('.form-container-chat').append(post)
    }
  };
  request.send();

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
    post.innerHTML = `<b> ${data["user"]} </b>: ${data["message"]} ${data["time"]}`;
    console.log('message sent');
    document.querySelector('.form-container-chat').append(post);
  });
});
