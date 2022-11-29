import base64

import requests

from src.MainApp.utils.FrameSource import FrameSource
from .base import BaseThread


class FrontThread(BaseThread):
    interval: float = 0.0
    camera: FrameSource = None

    def __init__(self, socket, cam_id=0):
        self.camera = FrameSource(cam_id)
        super().__init__(socket=socket)

    def run(self, **kwargs):
        self.camera.start()
        super().run(**kwargs)

    def work(self, **kwargs):
        try:
            source = kwargs['source']   # Data 불러오기
        except KeyError:
            source = {}

        # 카메라 사진 가져오기
        frame = self.camera.get_frame()
        b64_frame = base64.b64encode(frame)
        self.socket.emit('ui_front_pic', {'frame': b64_frame})       # UI 사진 갱신

        # 추론 진행
        res = requests.post('http://127.0.0.1:5001/front', data={
            'frame': b64_frame
        })
        res = res.json()
        source['front'] = res
