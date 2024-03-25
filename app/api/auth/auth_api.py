from flask import request, jsonify
from flask_jwt_extended import create_access_token, create_refresh_token, jwt_required, get_jwt_identity, get_jwt
from app.extensions import jwt, db
from flask_restx import Namespace, Resource, fields
from werkzeug.security import generate_password_hash, check_password_hash
from app.models import User

ns = Namespace('auth', description='Authentication')

user_model_register = ns.model('User_Register', {
    'firstname': fields.String(required=True, description='Prénom de l\'utilisateur'),
    'lastname': fields.String(required=True, description='Nom de l\'utilisateur'),
    'birthdate': fields.Date(required=True, description='Date de naissance de l\'utilisateur'),
    'email': fields.String(required=True, description='Email de l  \'utilisateur'),
    'password': fields.String(required=True, description='Mot de passe de l\'utilisateur')
})
user_model_login = ns.model('User_Login', {
    'email': fields.String(required=True, description='Email de l\'utilisateur'),
    'password': fields.String(required=True, description='Mot de passe de l\'utilisateur')
})

@ns.route('/register')
class Register(Resource):
    @ns.expect(user_model_register)
    def post(self):
        data = request.get_json()
        new_user = User(firstname=data['firstname'], lastname=data['lastname'], birthdate=data['birthdate'], email=data['email'])
        new_user.set_password(data['password'])

        if User.query.filter_by(email=data['email']).first():
            return {"message": "L'utilisateur existe déjà"}, 400
        

        db.session.add(new_user)
        db.session.commit()
        return {"message": "Utilisateur créé"}, 201
    
@ns.route('/login')
class Login(Resource):
    @ns.expect(user_model_login)
    def post(self):
        data = request.get_json()
        user = User.query.filter_by(email=data['email']).first()
        if user and user.check_password(data['password']):
            access_token = create_access_token(identity=user.id)
            refresh_token = create_refresh_token(identity=user.id)
            return {"access_token": access_token, "refresh_token": refresh_token}, 200
        return {"message": "Email ou mot de passe incorrect"}, 400


@ns.route('token/refresh')
class Refresh(Resource):
    @jwt_required(refresh=True)
    def post(self):
        current_user = get_jwt_identity()
        new_access_token = create_access_token(identity=current_user)
        return {"access_token": new_access_token}, 200