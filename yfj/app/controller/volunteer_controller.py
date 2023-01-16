from flask import Blueprint, jsonify, make_response, request, abort
from ..services.user_service import UserService

volunteer_controller = Blueprint('volunteer_controller', __name__, url_prefix='')

@volunteer_controller.route('/advices', methods=['POST'])
def create_user():
    if not request.json:
        abort(400)
    try:
        user_service = UserService()
        user_json = user_service.add(request.json)
    except Exception as err:
        return make_response(jsonify(err.args), 500)    
    return make_response(jsonify(user_json), 200)