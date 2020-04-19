import config
import sqlalchemy
from flask import Flask, json, request
from flask_cors import CORS, cross_origin
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = config.SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

def save(model):
    db.session.add(model)
    db.session.commit()

db.Model.save = save

from .routes.user import UserEndpoint

UserEndpoint(app)

@app.route('/healthcheck', methods=['GET'], strict_slashes=False)
def healthcheck():
  return json.dumps({'healthy': True}), 200
