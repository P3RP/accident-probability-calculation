from modules.source import Source


class ProbabilityCalc:
    default: float = 0.0

    def __init__(self, default):
        self.default = default

    # TODO: 사고 확률 계산하기
    def calc(self, source: Source):
        pass
