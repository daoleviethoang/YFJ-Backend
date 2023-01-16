""" This module contains the 'index' Blueprint which organize and
group, views related to the index endpoint of HTTP REST API.
"""


from flask import Blueprint, jsonify, make_response
from ..service.job_service import JobService

bp = Blueprint('index', __name__, url_prefix='')


@bp.route('/', methods=['GET'])
def index():
    """This function is responsible to deal with requests
    coming from index URL. It return a simple text indicating
    the server is running.

    Returns:
        str: a text message
    """
    #Add data from stats service to database and return jobs
    job_service = JobService()
    job_service.create()
    jobs = job_service.get_all()
    return make_response(jsonify([job.to_json() for job in jobs]), 200)

