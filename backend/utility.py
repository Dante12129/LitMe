import requests

from .constants import BOT


def sendToGroupMe(string):
    r = requests.post('https://api.groupme.com/v3/bots/post', data={'bot_id': BOT, 'text': string})
    return r.status_code
