from flask import Blueprint, request

from .utility import sendToGroupMe

messages = Blueprint('messages', __name__)


@messages.route('/process', methods=['POST'])
def process():
    data = request.get_json(force=True)
    text = data['text']

    if text.find('!echo') == 0:
        sendToGroupMe(text[6:])
    elif text.find('!poke') == 0:
        sendToGroupMe(f'{data["name"]} has poked {text[6:]}')

    return '{}', 200
