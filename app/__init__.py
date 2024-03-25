from flask import Flask
from .extensions import db, migrate, jwt, api_restx

def create_app():
    app = Flask(__name__)
    
    app.config.from_object('config.Config')

    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)
    api_restx.init_app(app)

    
    from .api.property.property_api import ns as property_ns
    from .api.users.user_api import ns as user_ns
    from .api.auth.auth_api import ns as auth_ns

    api_restx.add_namespace(property_ns, path='/api/property/properties')
    api_restx.add_namespace(user_ns, path='/api/users/users')
    api_restx.add_namespace(auth_ns, path='/api/auth/auth')

    return app
