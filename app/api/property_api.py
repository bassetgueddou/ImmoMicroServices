from flask import jsonify, request
from app import db, app
from app.models import property

@app.route('/api/properties', methods=['POST'])
def create_property():
    data = request.get_json()
    new_property = property.Property(
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

@app.route('/api/properties/city/<cityname>', methods=['GET'])
def get_properties_by_city(cityname):
    properties = property.query.filter_by(city=cityname).all()
    return jsonify([prop.to_dict() for prop in properties]), 200