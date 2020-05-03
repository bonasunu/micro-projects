document.addEventListener('DOMContentLoaded', () => {
    // Connect to websocket
    var socket = io.connect(location.protocol + '//' + document.domain + ':' + location.port);

    // active channel
    var activeChannel = "";

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

        // Clear input field
        document.querySelector("#channel").value = '';

        // Prevent form submission
        return false;
    };

    // Show list of channels
    socket.on('channel list', data => {
        if (data === "Channel exists") {
            alert("Channel exists");
        }
        else {
            let li = document.createElement('button');
            li.innerHTML = '# ' + data[data.length - 1];
            li.id = data[data.length - 1];
            li.className = 'button is-light'
            document.querySelector("#ch_list").append(li);
        };
        
    });

    // Show last channels
    socket.on('last channel', data => {
        for (let i = 0; i < data.length; i++) {
            let li = document.createElement('button');
            li.innerHTML = '# ' + data[i];
            li.id = data[i];
            li.className = 'button is-light'
            document.querySelector("#ch_list").append(li);
        };
    });
    
    // Implement join channel

    document.querySelector('#ch_list').addEventListener('click', function(e) {
        let clicked = e.target;
        if (clicked instanceof HTMLButtonElement) {
            let ch = clicked.id;
            socket.emit('join channel', ch);
        };
    });

    // Active channel
    socket.on('active channel', data => {
        activeChannel = data;
        document.querySelector('#sendMsg').disabled = false;
        document.querySelector('#message').innerHTML = "Message on Channel # " + data;
    });

    // Disable message send button if user not select any channel
    if (activeChannel == "") {
        document.querySelector('#sendMsg').disabled = true;
    };

    // TODO
    // Change message when user change channel
    // Send message
    document.querySelector('#sendMsg').onclick = () => {
        let msg = document.querySelector('#msg').value;

        socket.emit('message', msg);

        // Clear input field
        document.querySelector('#msg').value = '';

        return false;
    };

    // TODO
    // Change message when user change channel
    // Message area
    socket.on('message', data => {
        let p = document.createElement('p');
        p.innerHTML = data;
        document.querySelector('#msg_area').append(p);
    });

    // Delete data on LocalStorage
    //document.querySelector('#delete_data').onclick = () => {
    //    localStorage.clear();
    //};
}); 