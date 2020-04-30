document.addEventListener('DOMContentLoaded', () => {
    // Connect to websocket
    var socket = io.connect(location.protocol + '//' + document.domain + ':' + location.port);

    
    // Check localstorage for user info
    if (!localStorage.getItem('user')) {
        document.querySelector("#create_username").style.visibility = "visible";
        const warnUser = document.createElement("h2");
        warnUser.innerHTML = "Please create username before use Flack app!";
        warnUser.className = "subtitle";
        document.querySelector('#greet').append(warnUser);
    };

    document.querySelector('#create_username').onsubmit = () => {
        const username = document.querySelector('#new_username').value;
        localStorage.setItem('user', username);
        document.querySelector('#create_username').style.visibility = "hidden";

        return false;
    };
    
    // When connected, send info
    socket.on('connect', () => {
        if (localStorage.getItem('user')) {
            document.querySelector('#create_username').style.visibility = "hidden";
            let user = localStorage.getItem('user');
            socket.emit('user connected', {"user": user});
        };
    });

    // Send greeting message to user
    socket.on('greeting', data => {
        let hello = document.createElement('h2');
        hello.innerHTML = "Hello " + data + "!";
        hello.className = "subtitle";
        document.querySelector('#greet').append(hello);
    });

    // Create channel event
    document.querySelector("#create_channel").onsubmit = () => {
        // Emit the channel creation event using the input from the user
        const channel = document.querySelector("#channel").value;
        socket.emit("channel creation", channel);
        // Prevent form submission
        return false;
    };

    // Show list of channels
    socket.on('channel list', data => {
        let li = document.createElement('a');
        li.innerHTML = '# ' + data;
        li.className = 'panel-block';
        document.querySelector("#ch_list").append(li);
        
    });
}); 