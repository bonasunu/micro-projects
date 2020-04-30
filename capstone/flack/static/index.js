document.addEventListener('DOMContentLoaded', () => {
    // Connect to websocket
    var socket = io.connect(location.protocol + '//' + document.domain + ':' + location.port);

   

    // When connected, send info
    socket.on('connect', () => {
        let user = "Bona";
        
        socket.emit('user connected', {"user": user});
    });

    // Send greeting message to user
    socket.on('greeting', data => {
        let h2 = document.createElement("h2");
        h2.innerHTML = "Hello " + data;
        document.querySelector("#greet").append(h2);
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
        document.querySelector("#ch_list").append(li);
        
    });
}); 