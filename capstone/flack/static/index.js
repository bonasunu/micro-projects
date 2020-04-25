
document.addEventListener('DOMContentLoaded', () => {
    
    // Connect to websocket
    var socket = io.connect(location.protocol + '//' + document.domain + ':' + location.port);

    // Check if user exist when connected. Otherwise, call function to create it
    socket.on('connect', () => {

        document.querySelector('#hello').append('Connected');
        if (!localStorage.getItem('username')) {
            localStorage.setItem('username', 'Bonaventura');
        };

        const h2 = document.createElement('h2');
        h2.innerHTML = `Hello ${localStorage.getItem('username')}!`;
        document.querySelector('#hello').append(h2);
    });

    // Delete data
    document.querySelector('button').addEventListener('click', () => {
        localStorage.clear();
        while (document.querySelector('#hello').firstChild) {
            document.querySelector('#hello').removeChild(document.querySelector('#hello').firstChild);
        };
    });

});


