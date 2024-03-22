from flask import jsonify, request, make_response
from app import db, app
from app.models.property import Property


@app.route('/api/properties', methods=['POST'])
def create_property():
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

@app.route('/api/properties/<int:property_id>', methods=['PUT'])
def update_property(property_id):

    """Dans le cas ou l'authentification est basée sur un token par exemple, on pourrait vérifier l'identité du propriétaire de la propriété
    en vérifiant le token.
     exemple : current_user_id = get_current_user_id();
     if current_user_id != prop.owner_id: On refuse l'accès sinon on continue la modification...
    Ici, on simule cette vérification en vérifiant que l'id du propriétaire est passé en paramètre de la requête vu qu'on ne gère pas l'authentification dans ce projet. 
    """
    mock_owner_id = request.args.get('owner_id', type=int)
    if not mock_owner_id: 
        response = jsonify({"error": "id du proprio manquant dans la requête"})
        return make_response(response, 403)

    prop = Property.query.get_or_404(property_id)

    if prop.owner_id != mock_owner_id:
        response = jsonify({"error": "Accès refusé : vous n'êtes pas autorisé à modifier cette propriété"})
        return make_response(response, 403)

    data = request.get_json()

    if 'name' in data:
        prop.name = data['name']

    if 'description' in data:
        prop.description = data['description']

    if type in data:
        prop.type = data['type']

    if 'city' in data:
        prop.city = data['city']

    if 'rooms' in data:
        prop.rooms = data['rooms']
    
    
    db.session.commit()
    return jsonify(prop.to_dict()), 200


@app.route('/api/properties/city/<cityname>', methods=['GET'])
def get_properties_by_city(cityname):
    properties = Property.query.filter_by(city=cityname).all()
    return jsonify([prop.to_dict() for prop in properties]), 200