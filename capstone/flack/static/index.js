
document.addEventListener('DOMContentLoaded', () => {
    
    // Connect to websocket
    var socket = io.connect(location.protocol + '//' + document.domain + ':' + location.port);

    // Check if user exist when connected. Otherwise, call function to create it
    socket.on('connect', () => {

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

        // Create channel and add to channelList in app.py via "add channel" event
        document.querySelector('#createChannel').addEventListener('submit', () => {
            let chName = document.querySelector('#channelName').value;
            socket.emit('add channel', {'chName': chName});
        });

    });

    // Delete data on localStorage
    document.querySelector('button').addEventListener('click', () => {
        localStorage.clear();
        while (document.querySelector('#hello').firstChild) {
            document.querySelector('#hello').removeChild(document.querySelector('#hello').firstChild);
        };
    });

});


