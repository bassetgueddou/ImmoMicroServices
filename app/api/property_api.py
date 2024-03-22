from flask import jsonify, request, make_response
from app.extensions import db
from app.models.property import Property
from sqlalchemy import func
from flask_restx import Namespace, Resource

ns = Namespace('properties', description='Opérations sur les propriétés')

@ns.route('/create')
class PropertyCreate(Resource):
    """ Ici dans le cas ou l'authentification est en place, on pourrait vérifier l'identité du propriétaire ou de l'user afin de lui associer
    la prop créee."""

    @ns.doc('create_property')
    def post(self):
        
        """Crée un nouveau bien immo"""
        data = request.get_json()
        new_property = Property(
            name=data['name'],
            description=data['description'],
            type=data['type'],
            city=data['city'],
            rooms=data['rooms'],
            owner_id=data['owner_id']
        )
        db.session.add(new_property)
        db.session.commit()
        return jsonify(new_property.to_dict())

@ns.route('/edite/<int:property_id>')
@ns.param('property_id', 'L\'identifiant de la propriété')
@ns.param('owner_id', 'L\'identifiant du propriétaire', _in='query')
class PropertyEdit(Resource):
    """Dans le cas ou l'authentification est basée sur un token par exemple, on pourrait vérifier l'identité du propriétaire de la propriété
        en vérifiant le token.
        exemple : current_user_id = get_current_user_id();
        if current_user_id != prop.owner_id: On refuse l'accès sinon on continue la modification...
        Ici, on simule cette vérification en vérifiant que l'id du propriétaire est passé en paramètre de la requête vu qu'on ne gère pas l'authentification dans ce projet. """
    @ns.doc('update_property')
    def put(self, property_id):
        """Met à jour une propriété existante"""
        mock_owner_id = request.args.get('owner_id', type=int)
        if not mock_owner_id:
            return make_response({"erreur": "id du proprio manquant dans la requête"}, 403)
        prop = Property.query.get_or_404(property_id)

        if prop.owner_id != mock_owner_id:
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