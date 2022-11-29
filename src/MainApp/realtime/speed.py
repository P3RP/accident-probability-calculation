from flask_socketio import emit, SocketIO

from src.MainApp.modules import MainServer


def route_speed(socket: SocketIO, main_server: MainServer):
    @socket.on('gps')
    def speed(gps):
        print(gps)
        speed_info = main_server.calculator.elements['speed'].calc(
            lat=gps['lat'],
            lng=gps['lng'],
            timestamp=gps['timestamp'],
        )
        main_server.controller.data['speed'] = speed_info['info']['speed']
        main_server.calculator.data['speed'] = speed_info

        emit('ui_speed', {
            'speed': speed_info
        })
