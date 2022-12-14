from flask import Blueprint, Response
import json
import random


jobs = Blueprint('jobs', __name__, url_prefix='/jobs')

def get_three_random_jobs():
    with open('./application/api/jobs.json', 'r') as f:  #opens the json file to read from it
        #load the json file
        jobs_array = json.load(f)
        #return three random jobs from the json file  
        random_jobs = random.sample(jobs_array, 3)

    return random_jobs




@jobs.route('/')
def return_jobs():
    #get the three random jobs
    random_jobs = get_three_random_jobs()
    #return the jobs as json
    return Response(json.dumps(random_jobs), mimetype='application/json', status=200)





