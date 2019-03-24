from flask import Flask

from .api import api
from .messages import messages

app = Flask(__name__)


@app.route('/')
def index():
    return 'Nothing to see here.'


app.register_blueprint(api, url_prefix='/api')
app.register_blueprint(messages, url_prefix='/messages')
