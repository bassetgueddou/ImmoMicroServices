from flask import jsonify, request
from app import db, app
from app.models.user import User
from datetime import datetime


@app.route('/api/users', methods=['POST'])
def create_user():
    data = request.get_json()
    birthdate = datetime.strptime(data['birthdate'], '%Y-%m-%d').date()
    new_user = User(
        firstname=data['firstname'],
        lastname=data['lastname'],
        birthdate=birthdate
    )
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"id": new_user.id}), 201



@app.route('/api/users/<user_id>', methods=['PUT'])
def update_user(user_id):
    user = User.query.get_or_404(user_id)
    data = request.get_json()
    user.firstname = data.get('firstname', user.firstname)
    user.lastname = data.get('lastname', user.lastname)
    user.birthdate = datetime.strptime(data['birthdate'], '%Y-%m-%d').date()

    db.session.commit()
    return jsonify({"message": "Utilisateur modifié avec succès"}), 200