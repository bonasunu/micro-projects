document.addEventListener('DOMContentLoaded', () => {
    // Connect to websocket
    var socket = io.connect(location.protocol + '//' + document.domain + ':' + location.port);

    // When connected, send info
    socket.on('connect', () => {

        socket.emit('user connected', {"connected": "SocketIO is up and running"});
    });

    socket.on('myList', data => {
        let h2 = document.createElement("h2");
        h2.innerHTML = data;
        document.querySelector("body").append(h2);

    });
});