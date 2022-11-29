from flask import Blueprint, request


front = Blueprint('front_rt', __name__)


@front.route("/front", methods=['POST'])
def front():
    file = request.files['file']

    from src.PredictApp.app import front
    now_front = front.predict(file)

    return {
        'front': front
    }
