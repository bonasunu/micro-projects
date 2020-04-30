document.addEventListener('DOMContentLoaded', () => {
    // Connect to websocket
    var socket = io.connect(location.protocol + '//' + document.domain + ':' + location.port);

    
    // Check localstorage for user info
    if (!localStorage.getItem('user')) {
        document.querySelector("#create_username").style.visibility = "visible";
        const warnUser = document.createElement("h2");
        warnUser.innerHTML = "Please create username before use Flack app!";
        warnUser.className = "subtitle";
        warnUser.id = "warning"
        document.querySelector('#greet').append(warnUser);
    };

    document.querySelector('#create_username').onsubmit = () => {
        const username = document.querySelector('#new_username').value;
        localStorage.setItem('user', username);
        document.querySelector('#create_username').style.display = "none";
        document.querySelector('#warning').style.display = "none";
        socket.emit('user connected', {"user": username});
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
        hello.className = "title";
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
        li.innerHTML = '# ' + data[data.length - 1];
        li.className = 'panel-block';
        document.querySelector("#ch_list").append(li);
        
    });

    // Show last channels
    socket.on('last channels', data => {
        for (let i = 0; i < data.length; i++) {
            let li = document.createElement('a');
            li.innerHTML = '# ' + data[i];
            li.className = 'panel-block';
            document.querySelector("#ch_list").append(li);
        };
    });

    document.querySelector('#delete_data').onclick = () => {
        localStorage.clear();
    };
}); 