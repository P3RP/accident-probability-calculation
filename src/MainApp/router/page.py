from flask import render_template
from flask import Blueprint, request

page = Blueprint('page_rt', __name__)


@page.route("/", methods=['GET'])
def index():
    return render_template('index.html')


@page.route("/main", methods=['GET'])
def main():
    from src.MainApp.app import main_server

    param = request.args.to_dict()

    # 사용자 입력값 저장
    main_server.set_user(
        param['id'],
        int(param['sex']),
        int(param['age']),
        int(param['expr']),
    )

    return render_template('main.html')
