from typing import *

from .base import BaseCalc


class ActivityCalc(BaseCalc):
    label: List[str] = [
        "safe driving",
        "texting - right",
        "talking on the phone - right",
        "texting - left",
        "talking on the phone - left",
        "operating the radio",
        "drinking",
        "reaching behind",
        "hair and makeup",
        "talking to passenger",
    ]

    def calc(self, **kwargs):
        print(kwargs)
        act = kwargs['rt']['act']
        data = kwargs['data']

        prob = 0.0
        info = {
            'act': self.label[act]
        }

        match act:
            case 0:
                prob = 0.0      # 안전 운전
            case 1:
                prob = 15.0      # 문자 - 오른손
            case 2:
                prob = 15.0      # 전화 - 오른손
            case 3:
                prob = 15.0      # 문자 - 왼손
            case 4:
                prob = 15.0      # 전화 - 왼손
            case 5:
                prob = 5.0      # 라디오 조작
            case 6:
                prob = 10.0      # 물 마시기
            case 7:
                prob = 30.0      # 뒤 접근
            case 8:
                prob = 10.0      # 머리 정리
            case 9:
                prob = 5.0      # 옆 사람과 대화

        data['prob'] = prob
        data['info'] = info
