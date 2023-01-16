""" This module contains the 'index' Blueprint which organize and
group, views related to the index endpoint of HTTP REST API.
"""


from flask import Blueprint
from ..services.job_service import JobService

bp = Blueprint('index', __name__, url_prefix='')


@bp.route('/', methods=['GET'])
def index() -> str:
    """This function is responsible to deal with requests
    coming from index URL. It return a simple text indicating
    the server is running.

    Returns:
        str: a text message
    """
    #Add data from stats service to database
    job_service = JobService()
    results = job_service.create()
    return results


