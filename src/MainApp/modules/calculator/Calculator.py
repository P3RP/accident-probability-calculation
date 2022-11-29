from typing import *

from flask_socketio import SocketIO

from src.MainApp.dto import UserDTO
from .elements import *


class Calculator:
    default: float = -1
    prob: float = -1
    socket: SocketIO = None

    elements: Dict[str, BaseCalc] = {
        'activity': ActivityCalc(),
        'speed': SpeedCalc(),
        'front': FrontCalc(),
        'sleep': SleepCalc(),
    }
    data: Dict[str, Any] = {
        'speed': {
            'prob': 0.0,
            'info': {}
        },
        'front': {
            'prob': 0.0,
            'info': {}
        },
        'sleep': {
            'prob': 0.0,
            'info': {}
        },
        'activity': {
            'prob': 0.0,
            'info': {}
        },
    }

    def __init__(self, socket: SocketIO):
        self.socket = socket

    # Default 값 계산
    def calculate_df(self, user: UserDTO):
        calc = DefaultCalc()
        default = calc.calc(
            sex=user.sex,
            age=user.age,
            expr=user.expr
        )
        self.default = default
        self.prob = default

    # 실시간 요소 계산
    def calculate_rt(self, data):
        for element in self.elements.values():
            element.calc(rt=data, data=self.data)

    # 확률 계산
    def get_prob(self):
        total_prob = self.default
        dangers = []
        for danger, info in self.data.items():
            if info['prob'] > 0.0:
                dangers.append(danger)
                total_prob += info['prob']

        return {
            'prob': total_prob,
            'dangers': dangers
        }
