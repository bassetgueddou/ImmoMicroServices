from flask import jsonify, request, make_response
from app.extensions import db
from app.models.property import Property
from sqlalchemy import func
from flask_restx import Namespace, Resource, fields
from flask_jwt_extended import jwt_required, get_jwt_identity

ns = Namespace('properties', description='Opérations sur les propriétés')

property_model = ns.model('Property', {
    'name': fields.String(required=True, description='Nom du bien'),
    'description': fields.String(required=True, description='Description du bien'),
    'type': fields.String(required=True, description='Type de bien'),
    'city': fields.String(required=True, description='Ville où se trouve le bien'),
    'rooms': fields.Integer(required=True, description='Nombre de pièces')
})

@ns.route('/create')
class PropertyCreate(Resource):
   

    @ns.doc('create_property')
    @jwt_required()
    @ns.expect(property_model)
    def post(self):
        
        """Crée un nouveau bien immo"""
        current_user_id = get_jwt_identity()

        data = request.get_json()
        new_property = Property(
            name=data['name'],
            description=data['description'],
            type=data['type'],
            city=data['city'],
            rooms=data['rooms'],
            owner_id=current_user_id
        )
        db.session.add(new_property)
        db.session.commit()
        return jsonify(new_property.to_dict())

@ns.route('/edite/<int:property_id>')
@ns.param('property_id', 'L\'identifiant de la propriété')
class PropertyEdit(Resource):

    @ns.doc('update_property')
    @jwt_required()
    @ns.expect(property_model)

    def put(self, property_id):
        """Met à jour une propriété existante"""
        current_user_id = get_jwt_identity()

        prop = Property.query.get_or_404(property_id)

        if prop.owner_id != current_user_id:
            return make_response({"erreur": "Accès refusé : vous n'êtes pas autorisé à modifier cette propriété"}, 403)

        data = request.get_json()

        prop.name = data.get('name', prop.name)
        prop.description = data.get('description', prop.description)
        prop.type = data.get('type', prop.type)
        prop.city = data.get('city', prop.city)
        prop.rooms = data.get('rooms', prop.rooms)

        db.session.commit()
        return jsonify(prop.to_dict())

@ns.route('/<cityname>')
@ns.param('cityname', 'Le nom de la ville')
class PropertyListeByCity(Resource):
    @ns.doc('get_properties_by_city')
    def get(self, cityname):
        """Récupère les propriétés d'une ville donnée"""
        cityname_convertie = cityname.lower()
        properties = Property.query.filter(func.lower(Property.city) == cityname_convertie).all()
        return jsonify([prop.to_dict() for prop in properties])

@ns.route('/delete/<int:property_id>')
@ns.param('property_id', 'L\'identifiant de la propriété')
class PropertyDelete(Resource):
    @ns.doc('delete_property')
    @jwt_required()
    def delete(self, property_id):
        """Supprime une propriété"""
        current_user_id = get_jwt_identity()

        prop = Property.query.get_or_404(property_id)

        if prop.owner_id != current_user_id:
            return make_response({"erreur": "Accès refusé : vous n'êtes pas autorisé à supprimer cette propriété"}, 403)

        db.session.delete(prop)
        db.session.commit()
        return {"message": "Propriété supprimée avec succès"}, 200