import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config.from_object(os.environ['CURRENT_CONFIG'])

db = SQLAlchemy(app)

from . import models
from . import resources