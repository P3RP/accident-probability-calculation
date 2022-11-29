from typing import *

from gtts import gTTS
import playsound


class Feedback:
    msg: str = ''
    filename: str = 'msg.mp3'

    label: Dict[str, str] = {
        'activity': '운전에 적합하지 않은 행동 포착',
        'speed': '불안정한 속도 급변',
        'front': '차량 정면 교통 혼잡',
        'sleep': '졸음 운전 감지됨',
    }

    def alarm(self):
        tts = gTTS(text=self.msg, lang='ko')
        tts.save(self.filename)
        playsound.playsound(self.filename)

    def make_msg(self, prob: float, dangers: List[str]) -> None:
        self.msg = f'현재 발생 확률은 {prob}입니다.'
        self.msg += '현재 사고 위험요소로는 '
        for danger in dangers:
            self.msg += ', '.join(self.label[danger])
        self.msg += '이 있습니다. 안전한 운전을 위해 조심하십시오.'
