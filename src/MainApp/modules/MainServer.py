from typing import *

from threading import Timer, Event

from flask_socketio import SocketIO

from src.MainApp.dto import *
from .datacontroller import DataCollector
from .calculator import Calculator
from .Feedback import Feedback


class MainServer:
    user: Optional[UserDTO] = None
    socket: SocketIO = None
    _limit: float = 0.0
    __end_event: Event = None

    def __init__(self, socket: SocketIO):
        self.calculator: Calculator = Calculator(socket)
        self.controller: DataCollector = DataCollector()
        self.feedback: Feedback = Feedback()

        self.socket = socket

        self.__end_event = Event()

    # 시작
    def run(self):
        print('Main Server 시작')
        self.__end_event.clear()               # 종료 이벤트 초기화
        self.controller.run(self.socket)       # 실시간 관리 시작

        def set_interval(func, sec, *param):
            def func_wrapper():
                set_interval(func, sec, *param)
                func(*param)

            t = Timer(sec, func_wrapper)
            t.start()

            # 종료 조건
            if self.__end_event.is_set():
                print('Main Server Thread 종료')
                t.cancel()

            return t

        set_interval(self.__run_inner, 0.5)     # 0.5초 간격 확률 확인 실행

    def __run_inner(self):
        data = self.controller.get_data()
        current = self.calculator.calculate_rt(data)

        self.socket.emit('ui_prob', current)
        
        # 사고 확률 초과 시 알림
        if current['prob'] >= self._limit:
            self.feedback.make_msg(current['prob'], current['dangers'])
            self.feedback.alarm()

    # 종료
    def stop(self):
        self.__end_event.set()      # 종료 이벤트 실행
        self.controller.stop()      # 실시간 관리 종료
        self.user = None            # 유저 초기화

        print('Main Server 종료')

    def set_user(self, user_id: str, sex: int, age: int, expr: int):
        self.user = UserDTO(user_id, sex, age, expr)

    def set_default(self):
        self.calculator.calculate_df(self.user)

    def set_limit(self, limit):
        self._limit = limit
