
document.addEventListener('DOMContentLoaded', () => {

    createUser();
    function createUser() {

        // To do - Implement Local Storage
        if (!localStorage.getItem('user')) {
    
            var userInput = prompt("Input your username")
            localStorage.setItem('user', userInput);
            
        };
    };
    
    // Connect to websocket
    var socket = io.connect(location.protocol + '//' + document.domain + ':' + location.port);

    // Check if user exist when connected. Otherwise, call function to create it
    socket.on('connect', () => {

        const h2 = document.createElement('h2');
        h2.innerHTML = `Hello ${userInput}!`;
        document.querySelector('#hello').append(h2);
        document.Elem

    });

    document.querySelector('#deleteData').onClick = () => {
        localStorage.clear();
        const h2 = document.querySelector('h2');
        h2.remove();
        createUser();
    };
});
