from flask import Blueprint, jsonify, make_response, request, abort
from ..service.student_service import StudentService
from ..service.user_service import UserService
from ..models import UserCategoryEnum

user_controller = Blueprint('user_controller', __name__, url_prefix='')

@user_controller.route('/<username>/user', methods=['DELETE'])
def delete(username):
    try:
        user_service = UserService()
        results = user_service.delete(username)
    except Exception as err:
        print(err.args)
        abort(404)
    return make_response(jsonify(results), 200)

@user_controller.route('/<username>/user', methods=['GET'])
def get(username):
    try:
        user_service = UserService()
        results = user_service.get_by_username(username)
    except Exception as err:
        print(err.args)
        abort(404)
    return make_response(jsonify(results), 200)