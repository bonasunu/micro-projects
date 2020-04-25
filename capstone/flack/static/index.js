
document.addEventListener('DOMContentLoaded', () => {
    
    // Connect to websocket
    var socket = io.connect(location.protocol + '//' + document.domain + ':' + location.port);

    // Check if user exist when connected. Otherwise, call function to create it
    socket.on('connect', () => {

        document.querySelector('#hello').append('Connected');
        if (!localStorage.getItem('username')) {
            document.querySelector('#form').style.visibility = 'visible';
            document.querySelector('#form').addEventListener('submit', () => {
                let user = document.querySelector('#userInput').value;
                localStorage.setItem('username', user);
            });
            
        }
        else {
            document.querySelector('#form').style.visibility = 'hidden';
            const h2 = document.createElement('h2');
            h2Value = localStorage.getItem('username');
            h2.innerHTML = 'Hello ' + h2Value;
            document.querySelector('#hello').append(h2);
        };

    });

    // Delete data on localStorage
    document.querySelector('button').addEventListener('click', () => {
        localStorage.clear();
        while (document.querySelector('#hello').firstChild) {
            document.querySelector('#hello').removeChild(document.querySelector('#hello').firstChild);
        };
    });

});


