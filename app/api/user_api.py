from flask_restx import Namespace, Resource
from flask import jsonify, request
from app.extensions import db
from app.models.user import User
from datetime import datetime
from flask_restx import fields


ns = Namespace('users', description='Opérations liées aux utilisateurs')

user_model = ns.model('User', {
    'firstname': fields.String(required=True, description='Prénom de l\'utilisateur'),
    'lastname': fields.String(required=True, description='Nom de l\'utilisateur'),
    'birthdate': fields.Date(required=True, description='Date de naissance de l\'utilisateur')
})

@ns.route('/create')
class UserCreate(Resource):
    @ns.expect(user_model)
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
    @ns.expect(user_model)
    def put(self, user_id):
        user = User.query.get_or_404(user_id)
        data = request.get_json()
        user.firstname = data.get('firstname', user.firstname)
        user.lastname = data.get('lastname', user.lastname)
        user.birthdate = datetime.strptime(data['birthdate'], '%Y-%m-%d').date()

        db.session.commit()
        return {"message": "Utilisateur modifié avec succès"}, 200
