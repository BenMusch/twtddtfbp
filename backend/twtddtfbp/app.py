from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from twtddtfbp.config import BaseConfig

app = Flask(__name__)
app.config.from_object(BaseConfig)

db = SQLAlchemy(app)
migrate = Migrate(app, db)


from twtddtfbp.models import *

@app.route('/hello/', methods=['GET'])
def hello():
    return ('Hello, world', 200)
