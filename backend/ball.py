from flask import Blueprint
import random

ball = Blueprint('ball', __name__, template_folder='../frontend')

responses = ["It is certain",
             "Without a doubt",
             "You may rely on it",
             "Yes definitely"]


@ball.route('/ball', methods=['GET'])
def show_ball():
    return random.choice(responses)
