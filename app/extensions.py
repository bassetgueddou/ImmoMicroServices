from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from flask_restx import Api

db = SQLAlchemy()
migrate = Migrate()
jwt = JWTManager()
api_restx = Api(version='1.0', title='Immo API', description='A Property Management API')