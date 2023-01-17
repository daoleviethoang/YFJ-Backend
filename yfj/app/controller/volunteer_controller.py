from flask import Blueprint, jsonify, make_response, request, abort
from ..service.user_service import UserService
from ..service.volunteer_service import VolunteerService
from ..models import UserCategoryEnum

volunteer_controller = Blueprint('volunteer_controller', __name__, url_prefix='')

@volunteer_controller.route('/jobs', methods=['POST'])
def create():
    if not request.json or request.json.get("role") != UserCategoryEnum.Volunteer.name:
        abort(400)
    try:
        volunteer_service = VolunteerService()
        user_json = volunteer_service.add(request.json)
    except Exception as err:
        print(err)
        return make_response(jsonify(err.args), 500)    
    return make_response(jsonify(user_json), 200)

@volunteer_controller.route('/<username>/jobs', methods=['PATCH'])
def update(username):
    if not request.json:
        abort(400)
    try:
        volunteer_service = VolunteerService()
        results = volunteer_service.update(request.json, username)
    except Exception as err:
        print(err.args)
        abort(400)
    return make_response(jsonify(results), 200)