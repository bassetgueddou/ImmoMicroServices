from flask_restx import Namespace, Resource
from flask import jsonify, request
from app.extensions import db
from app.models.user import User
from datetime import datetime

ns = Namespace('users', description='Opérations liées aux utilisateurs')

@ns.route('/create')
class UserCreate(Resource):
    def post(self):
        data = request.get_json()
        birthdate = datetime.strptime(data['birthdate'], '%Y-%m-%d').date()
        new_user = User(
            firstname=data['firstname'],
            lastname=data['lastname'],
            birthdate=birthdate
        )
        db.session.add(new_user)
        db.session.commit()
        return {"Utilisateur créé, id": new_user.id}, 201

@ns.route('/edite/<int:user_id>')
@ns.param('user_id', 'L\'identifiant de l\'utilisateur')
class UserEdit(Resource):
    def put(self, user_id):
        user = User.query.get_or_404(user_id)
        data = request.get_json()
        user.firstname = data.get('firstname', user.firstname)
        user.lastname = data.get('lastname', user.lastname)
        user.birthdate = datetime.strptime(data['birthdate'], '%Y-%m-%d').date()

        db.session.commit()
        return {"message": "Utilisateur modifié avec succès"}, 200
