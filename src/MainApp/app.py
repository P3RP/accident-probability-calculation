from flask import Flask
from flask_socketio import SocketIO

from src.MainApp.modules import MainServer
from src.MainApp.router import register_router
from src.MainApp.realtime import register_socket_event

import eventlet
eventlet.monkey_patch()

# App 설정
app = Flask(__name__)
app.secret_key = 'password'

# Socket IO로 등록
socket = SocketIO()
socket.init_app(app, logger=True, async_mode='eventlet')

# 중앙 서버 등록
main_server = MainServer(socket=socket)


if __name__ == '__main__':
    register_router(app)
    register_socket_event(socket, main_server)
    socket.run(app, debug=True)
