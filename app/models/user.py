from app import db
from datetime import datetime

class User(db.Model):
   id = db.Column(db.Integer, primary_key=True)
   firstname = db.Column(db.String(50), nullable=False)
   lastname = db.Column(db.String(50), nullable=False)
   birthdate = db.Column(db.DateTime, nullable=False)