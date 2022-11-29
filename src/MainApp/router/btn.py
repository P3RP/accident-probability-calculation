from flask import Blueprint


btn = Blueprint('btn_rt', __name__)


@btn.route("/start", methods=['POST'])
def start():
    from src.MainApp.app import main_server

    main_server.run()

    return 'Start'


@btn.route("/stop", methods=['POST'])
def stop():
    from src.MainApp.app import main_server

    main_server.stop()

    return 'Stop'
