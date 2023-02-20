function connect_MTserver(MTserver, nickname) {
    var socket = new WebSocket(MTserver);
    socket.addEventListener('open', function (event) {
        socket.send("{'connect': " + nickname + "}")
        return {'connect': nickname};
    });
}

function send_info(str_x, str_y, ztr_z, nickname) {
    socket.send("{'x': " + str_x + ", 'y': " + str_y + ", 'z': " + str_z + ", 'nickname': " + "nickname}");
    return {'x': str_x, 'y': str_y, 'z': str_z, 'nickname': nickname};
}

function get_info() {
    socket.addEventListener('message', function(event) {
        let data = JSON.parse(event.data);
        return data;
    })
}