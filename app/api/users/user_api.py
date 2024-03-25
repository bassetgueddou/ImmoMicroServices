from flask_restx import Namespace, Resource
from flask import request
from app.extensions import db
from app.models.user import User
from datetime import datetime
from flask_restx import fields
from flask_jwt_extended import jwt_required, get_jwt_identity


ns = Namespace('users', description='Opérations liées aux utilisateurs')

user_model = ns.model('User', {
    'firstname': fields.String(required=True, description='Prénom de l\'utilisateur'),
    'lastname': fields.String(required=True, description='Nom de l\'utilisateur'),
    'birthdate': fields.Date(required=True, description='Date de naissance de l\'utilisateur'),
})



@ns.route('/edite_profile')
class UserEdit(Resource):
    @jwt_required()
    @ns.expect(user_model)
    def put(self):
        current_user_id = get_jwt_identity()
        user = User.query.get_or_404(current_user_id)
        data = request.get_json()
        user.firstname = data.get('firstname', user.firstname)
        user.lastname = data.get('lastname', user.lastname)
        user.birthdate = datetime.strptime(data['birthdate'], '%Y-%m-%d').date()

        db.session.commit()
        return {"message": "Utilisateur modifié avec succès"}, 200
