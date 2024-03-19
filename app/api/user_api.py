from flask import jsonify, request
from app import db, app
from app.models import user

@app.route('/api/<user_id>/user', methods=['PUT'])
def update_user(user_id):
    user = user.query.get_or_404(user_id)
    data.request.get_json()
    user.first_name = data.get('first_name', user.first_name)
    user.last_name = data.get('last_name', user.last_name)

    db.session.commit()
    return jsonify({"message": "Utilisateur modifié avec succès"}), 200