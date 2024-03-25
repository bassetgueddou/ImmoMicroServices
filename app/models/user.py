from app import db
from datetime import date
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
   id = db.Column(db.Integer, primary_key=True)
   firstname = db.Column(db.String(50), nullable=False)
   lastname = db.Column(db.String(50), nullable=False)
   birthdate = db.Column(db.Date, nullable=False)
   email = db.Column(db.String(120), unique=True, nullable=False)
   password_hash =   db.Column(db.TEXT, nullable=False)

   def set_password(self, password):
      self.password_hash = generate_password_hash(password)

   def check_password(self, password):
      return check_password_hash(self.password_hash, password)

   def to_dict(self):
         return {
            "id": self.id,
            "firstname": self.firstname,
            "lastname": self.lastname,
            "birthdate": self.birthdate.strftime('%Y-%m-%d') if self.birthdate else None
         }