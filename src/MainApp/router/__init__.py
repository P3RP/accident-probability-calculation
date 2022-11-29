from flask import Flask

from .page import page as page_rt
from .btn import btn as btn_rt


# Router 등록
def register_router(flask_app: Flask):
    flask_app.register_blueprint(page_rt)
    flask_app.register_blueprint(btn_rt)
