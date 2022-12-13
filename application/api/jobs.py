from flask import Blueprint, Response
import json
from Jobs_dictionary import all_jobs



jobs = Blueprint('jobs', __name__, url_prefix='/jobs')

@jobs.route('/')
def job_displayer():
    result = all_jobs
    print(json.dumps(result))





