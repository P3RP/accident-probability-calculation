import datetime

from .base import BaseCalc


class DefaultCalc(BaseCalc):
    init: int = 20

    def calc(self, **kwargs):
        sex = kwargs['sex']
        age = kwargs['age']
        expr = kwargs['expr']

        add = 1.0

        # --------- 인적 사항 ---------
        # 성별 (남성)
        if sex == '1':
            add *= 1.05

        # 연령대
        age_group = age // 10
        if age_group in (4, 5):
            add *= 1.2
        elif age >= 65:
            add *= 1.1

        # 운전 경력
        if expr < 5:
            add *= 1.15
        elif 5 <= expr < 10:
            add *= 1.1
        elif 10 <= expr < 15:
            add *= 1.05

        # --------- 시간 ---------
        now = datetime.datetime.now()
        now.weekday()

        # 월별
        if now.month in (7, 10, 11):
            add *= 1.05

        # 요일별
        weekday = now.weekday()
        if weekday == 4:
            add *= 1.2
        elif weekday in (3, 5):
            add *= 1.1

        # 시간별
        if now.hour in (18, 19, 20):
            add *= 1.2
        elif now.hour in (14, 15, 16, 17):
            add *= 1.1

        return self.init * add
