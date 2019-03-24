from flask import Flask

from . import api

app = Flask(__name__)
bot = 'd742ebeb1264cf17890ffa913e'


@app.route('/')
def index():
    return 'Nothing to see here.'


app.register_blueprint(api, url_prefix='/api')
