from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from twtddtfbp.config import BaseConfig

app = Flask(__name__)
app.config.from_object(BaseConfig)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from twtddtfbp import cache, queries

cache.set('test_key', 0)

@app.route('/hello/', methods=['GET'])
def hello():
    return ('Hello, world', 200)

@app.route('/', methods=['GET'])
def index():
    val = cache.get('test_key')
    cache.set('test_key', val + 1)
    return ('Val: ' + str(val), 200)
