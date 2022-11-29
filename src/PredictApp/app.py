from flask import Flask

from .router import *
from .modules import *


# Router 등록
def register_router(flask_app: Flask):
    flask_app.register_blueprint(act_rt)
    flask_app.register_blueprint(front_rt)


activity = ActivityClassifier('./weight/act.pth')
front = FrontRecognition('./weight/front.pth')


if __name__ == '__main__':
    app = Flask(__name__)
    register_router(app)
    app.run(debug=True, port=5001)
