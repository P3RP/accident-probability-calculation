from typing import *

from flask_socketio import SocketIO

from .elements import *


class DataCollector:
    data: Dict[str, Any] = {}
    thread_list: List[Type[BaseThread]] = [
        FrontThread,
        ActivityThread
    ]
    running: List[BaseThread] = []

    def get_data(self):
        return self.data

    # 실시간 관리 시작
    def run(self, socket: SocketIO):
        for th in self.thread_list:
            worker = th(socket)     # 각 Thread Worker 생성
            worker.run(source=self.data)
            self.running.append(worker)

    # 실시간 관리 종료
    def stop(self):
        print(self.running)
        for worker in self.running:
            worker.stop()
        self.running.clear()
        print(self.running)
