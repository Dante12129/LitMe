from flask import Blueprint, request, redirect, url_for
import requests

from .constants import BOT

api = Blueprint('api', __name__)


def sendToGroupMe(string):
    r = requests.post('https://api.groupme.com/v3/bots/post', data={'bot_id': BOT, 'text': string})
    return r.status_code


@api.route('/post', methods=['POST'])
def post():
    data = request.get_json(force=True)
    if data is not None:
        message = data.get('message')
        return '{}', sendToGroupMe(message)
    return '{}', 200


@api.route('/dinner', methods=['POST'])
def dinner():
    sendToGroupMe('Someone wants to go to dinner.')
    return '[]', 200
