document.addEventListener('DOMContentLoaded', () => {
    // Connect to websocket
    var socket = io.connect(location.protocol + '//' + document.domain + ':' + location.port);

   

    // When connected, send info
    socket.on('connect', () => {
        let user = "Bona";

        socket.emit('user connected', {"user": user});
    });

    socket.on('greeting', data => {
        let h2 = document.createElement("h2");
        h2.innerHTML = "Hello " + data;
        document.querySelector("#greet").append(h2);
    });


    document.querySelector("#create_channel").onsubmit = () => {
        // Emit the channel creation event using the input from the user
        const channel = document.querySelector("#channel").value;
        socket.emit("channel creation", channel);
        // Prevent form submission
        return false;
    };

    socket.on('channel list', data => {
        let h3 = document.createElement("h3");
        h3.innerHTML = data;
        document.querySelector("body").append(h3);
    });
});