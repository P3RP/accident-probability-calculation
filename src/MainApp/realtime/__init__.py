from flask_socketio import SocketIO

from .speed import route_speed
from ..modules import MainServer


# Socket Event 등록
def register_socket_event(socket: SocketIO, main_server: MainServer):
    route_speed(socket, main_server)
