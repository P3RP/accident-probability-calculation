from typing import *

from .base import BaseCalc


class SleepCalc(BaseCalc):
    def calc(self, **kwargs):
        rt = kwargs['rt']
        data = kwargs['data']

        # 결과 변수
        prob = 0.0
        info = {
            'sleep': 0,
        }

        # 행동에 의한 졸음운전 수치 파악
        sleep = rt['activity']['sleep']

        # 교통 혼잡도에 따른 졸음 수치 파악
        if data['front']['info']['congestion'] > 60:    # 혼잡한 경우
            dist = rt['front']['dist']                  # 앞 차와의 거리
            if data['speed']['info']['speed'] - dist > 20:
                sleep += (data['speed']['info']['speed'] - dist) * 0.7

        else:   # 안 혼잡한 경우
            if data['speed']['info']['chg'] > 30:
                sleep += data['speed']['info']['chg'] * 0.7

        # 확률 계산
        if 0 < sleep <= 20:
            prob = 5.0
        elif 20 < sleep <= 40:
            prob = 8.0
        elif 40 < sleep <= 60:
            prob = 15.0
        elif 60 < sleep <= 100:
            prob = 30.0
        elif 80 < sleep <= 100:
            prob = 70.0

        # 결과 입력
        info['sleep'] = sleep
        data['front'] = {
            'prob': prob,
            'info': info,
        }
