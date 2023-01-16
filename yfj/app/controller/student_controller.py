from flask import Blueprint, jsonify, make_response, request, abort
from ..services.user_service import UserService

student_controller = Blueprint('student_controller', __name__, url_prefix='')

@student_controller.route('/<username>/advices', methods=['GET'])
def get_advices(username):
    try:
        user_service = UserService()
        results = user_service.get_by_username(username)
    except Exception as err:
        print(err.args)
        abort(404)
    return make_response(jsonify(results), 200)

@student_controller.route('/<username>/advices', methods=['PATCH'])
def update(username):
    if not request.json:
        abort(400)
    try:
        user_service = UserService()
        results = user_service.update(request.json, username)
    except Exception as err:
        print(err.args)
        abort(400)
    return make_response(jsonify(results), 200)

@student_controller.route('/advices', methods=['POST'])
def create_user():
    if not request.json:
        abort(400)
    try:
        user_service = UserService()
        user_json = user_service.add(request.json)
    except Exception as err:
        return make_response(jsonify(err.args), 500)    
    return make_response(jsonify(user_json), 200)

