document.addEventListener('DOMContentLoaded', () => {

    // Connect to websocket
    var socket = io.connect(location.protocol + '//' + document.domain + ':' + location.port);

    // Check if user exist when connected. Otherwise, call function to create it
    socket.on('connect', () => {

        // To do - Implement Local Storage

        const h2 = document.createElement('h2');
        h2.innerHTML = "Hello!";
        document.querySelector('#hello').append(h2);

    });

});