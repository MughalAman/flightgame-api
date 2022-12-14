<<<<<<< Updated upstream
from flask import Blueprint, Response
import os
=======
from flask import Blueprint, Response, request
>>>>>>> Stashed changes
import json
import itertools


leaderboard = Blueprint('leaderboard', __name__, url_prefix='/leaderboard')

<<<<<<< Updated upstream

@leaderboard.route('/')
def get_leaderboard():
    file_path = os.path.join(os.path.dirname(__file__), 'leaderboard.json')
    with open(file_path, 'r') as f:
        data = json.load(f)
    return json.dumps(data)
=======
def get_leaderboard():
    #returns a list of all the scores in json with the player name, the player country, the player score & how long the player took to finish the game in seconds

    # sorted by score
    # no duplicates
    # only the highest score for the player is returned

    with open('./application/api/leaderboard.json', 'r') as f: #opens the json file to read from it
        leaderboard_dict = json.load(f) #load the json file
        leaderboard_dict = sorted(leaderboard_dict, key=lambda k: k['player_score'], reverse=True) #sort the json file by score
        #filter out the duplicates that have the same player name, player country and a lower score
        leaderboard_dict = list(filter(lambda x: int(x['player_score']) == max([int(y['player_score']) for y in leaderboard_dict if y['player_name'] == x['player_name'] and y['player_country_code'] == x['player_country_code']]), leaderboard_dict))

        return leaderboard_dict



def save_leaderboard(player_name, player_country, player_score, player_time):
    #saves the player's score to the leaderboard json file
    
    with open('./application/api/leaderboard.json', 'r') as f: #opens the json file to read from it
        leaderboard_dict = json.load(f) #load the json file
        leaderboard_dict.append({'player_name': player_name, 'player_country': player_country, 'player_score': player_score, 'player_time': player_time}) #adds the player's score to the json file

        with open('leaderboard.json', 'w') as f: #opens the json file to write to it
            json.dump(leaderboard_dict, f, indent=4) #saves the json file

@leaderboard.route('/', methods=['GET', 'POST'])
def return_leaderboard():
    if request.method == 'GET':
        leaderboard_dict = get_leaderboard()
        return Response(json.dumps(leaderboard_dict), mimetype='application/json', status=200)
    elif request.method == 'POST':
        player_name = request.args.get('player_name')
        player_country = request.args.get('player_country')
        player_score = request.args.get('player_score')
        player_time = request.args.get('player_time')
        save_leaderboard(player_name, player_country, player_score, player_time)

        leaderboard_dict = get_leaderboard()
        return Response(json.dumps(leaderboard_dict), mimetype='application/json', status=200)
>>>>>>> Stashed changes
