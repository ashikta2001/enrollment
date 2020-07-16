from flask import Flask
from config import Config
from flask_mongoengine import MongoEngine
from flask_restplus import Api
from werkzeug.utils import cached_property

api=Api()

app = Flask(__name__)
app.config.from_object(Config)

db=MongoEngine()
db.init_app(app)
api.init_app(app)

from application import routes

