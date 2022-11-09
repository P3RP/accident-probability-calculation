import json

from flask import Flask, render_template, jsonify
from flask import request, Response


app = Flask(__name__)

import random


from modules.calculation import SpeedCalc

# f = FrameSource()
# f.start()

import cv2
camera = cv2.VideoCapture(0)


# 속도 계산 모듈
speed = SpeedCalc()


def gen_frames():
    while True:
        success, frame = camera.read()  # read the camera frame
        if not success:
            break
        else:
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')  # concat frame one by one and show result


# 메인 페이지
@app.route('/')
def index():
    return render_template("index.html")


# 동작하는 페이지
@app.route('/run', methods=['POST'])
def run():
    # TODO: 입력 받은 데이터 기반 기초 확률 세팅

    # TODO: 카메라 입력받아서 값 갱신하는 Thread 생성

    return render_template("run.html")


# TODO: 종료 버튼 누르기
@app.route('/stop', methods=['POST'])
def stop():
    return render_template("index.html")


# ======================================================
# 주기적으로 계속 호출되는 API
# ======================================================

# GPS 좌표를 가져오는 API
@app.route('/gps', methods=['POST'])
def gps():
    data = json.loads(request.get_data())

    # TODO: GPS 좌표 갱신 및 속도 데이터 갱신
    now_speed = speed.calc(*[float(x) for x in data.values()])

    return jsonify({'speed': now_speed})


# 사고 확률 제공 API
@app.route('/probability', methods=['GET'])
def get_probability():

    return jsonify({'prob': random.randint(1, 100), 'dangers': ['테스트'] * random.randint(1, 5)})


@app.route('/video')
def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == '__main__':
    app.run(debug=True)
