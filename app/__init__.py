from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

#Configuration de la bdd
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:basset@localhost:5432/Immodb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app.models import user, property
from app.api import property_api, user_api