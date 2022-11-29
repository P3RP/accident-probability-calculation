from flask import Blueprint, request


activity = Blueprint('act_rt', __name__)


@activity.route("/act", methods=['POST'])
def act():
    file = request.files['file']

    from src.PredictApp.app import activity
    now_act = activity.predict(file)

    return {
        'act': now_act
    }
