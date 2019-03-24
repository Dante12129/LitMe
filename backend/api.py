from flask import Blueprint, request

from .utility import sendToGroupMe

api = Blueprint('api', __name__)


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
