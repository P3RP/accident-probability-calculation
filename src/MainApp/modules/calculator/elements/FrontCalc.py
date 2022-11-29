from typing import *

from .base import BaseCalc


class FrontCalc(BaseCalc):
    def calc(self, **kwargs):
        # 정면 객체 수 확인
        rt = kwargs['rt']['front']
        data = kwargs['data']

        # 결과 변수
        prob = 0.0
        info = {
            'obj': 0,
            'area': 0.0,
            'congestion': 0.0
        }

        # 사물 갯수
        obj = rt['obj']
        info['obj'] = obj

        # 교통 가능 영역
        able = rt['able']
        area = able / 460800 * 100
        info['area'] = area

        # 교통 혼잡도 계산
        free_drive = area
        if obj > 3:
            free_drive *= 2
            free_drive /= obj
        congestion = 100 - free_drive
        info['congestion'] = congestion

        # 확률 계산
        if 0 < congestion <= 20:
            prob = 5.0
        elif 20 < congestion <= 40:
            prob = 8.0
        elif 40 < congestion <= 60:
            prob = 10.0
        elif 60 < congestion <= 80:
            prob = 13.0
        elif 80 < congestion <= 100:
            prob = 15.0

        # 결과 입력
        data['front'] = {
            'prob': prob,
            'info': info,
        }
