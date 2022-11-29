import time
from threading import Thread, Event

from flask_socketio import SocketIO


class BaseThread(object):
    interval: float = 1.0
    thread: Thread = None
    socket: SocketIO = None
    _end_event: Event = None

    def __init__(self, socket):
        self._end_event = Event()
        self.socket = socket

    def run(self, **kwargs):
        thread = Thread(target=self.__inner, kwargs=kwargs)
        thread.daemon = True                       # Daemonize thread
        thread.start()                             # Start the execution

    def __inner(self, **kwargs):
        while True:
            time.sleep(self.interval)
            if self._end_event.is_set():
                print(f'{self.__class__.__name__} Stop!')
                return

            # 작업 수행
            self.work(**kwargs)

    def stop(self):
        self._end_event.set()

    def work(self, **kwargs):
        raise Exception('Thread 내부 동작 함수 work()가 구현되지 않았습니다.')
