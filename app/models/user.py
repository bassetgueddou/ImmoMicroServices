from app import db
from datetime import date


class User(db.Model):
   id = db.Column(db.Integer, primary_key=True)
   firstname = db.Column(db.String(50), nullable=False)
   lastname = db.Column(db.String(50), nullable=False)
   birthdate = db.Column(db.Date, nullable=False)

   def to_dict(self):
         return {
            "id": self.id,
            "firstname": self.firstname,
            "lastname": self.lastname,
            "birthdate": self.birthdate.strftime('%Y-%m-%d') if self.birthdate else None
         }