# <b>Flightgame-API</b>
api for a school project game made in python using flask

<br>
<br>

# Table of Contents
- [Installation](#installation) WIP
- [Usage](#usage) WIP
- [Design](#design)

<br>
<br>

# Installation
### Create a virtual environment (optional)
```bash
python -m venv env
```

### Installing the required packages
```bash
pip install -r requirements.txt
```

<br>

# Usage
### Running the server locally
```bash
python app.py
```

<br>


# Design

## Routes
- [/countries](#get-countries)
- [/jobs](#get-jobs)
- [/weather](#get-weathercountry_name)
- [/leaderboard GET](#get-leaderboard)
- [/leaderboard POST](#post-leaderboard)

#
#### GET /countries
    returns a list of countries in json with country code, distance from the current location in meters, coordinates & the price to travel to that country

```json
[
    {
        "country_code": "FI",
        "distance_m": 5000000000,
        "coordinates": {
            "lat": 60.192059,
            "lon": 24.945831
        },
        "price": 500
    },
]
````

#

### GET /jobs

    returns a list of jobs in json with job name, is the job bad or good, the reward for the job & the penalty message for the job

```json
[
    {
        "job_name": "rob bank",
        "is_bad": true,
        "reward": 1000,
        "penalty_message": "you got caught and went to jail"
    },
]
```

#

### GET /weather/<country_name>

    returns the weather in the country in json with the temperature in celsius & the wind speed in m/s

```json
{
    "temperature": 20,
    "wind_speed": 10
}
```

#

### GET /leaderboard

    returns a list of all the scores in json with the player name, the player country, the player score & how long the player took to finish the game in seconds
    
    // sorted by score
    // no duplicates
    // only the highest score for the player is returned


```json
[
    {
        "player_name": "player1",
        "player_country_code": "FI",
        "player_score": 1000,
        "finish_time": 300
    },
]
```

#

### POST /leaderboard

    adds a new score to the leaderboard

    // duplicates are allowed
    // returns the new leaderboard

request body:

```json
{
    "player_name": "player1",
    "player_country_code": "FI",
    "player_score": 1000,
    "finish_time": 300
}
```

response body:

```json
[
    {
        "player_name": "player1",
        "player_country_code": "FI",
        "player_score": 1000,
        "finish_time": 300
    },
]
```
# Credits
### The team behind this project
- [Aman Mughal](https://amppa.dev/)
- [Santtu Karhu](https://github.com/JSABear/)
- [Mixu Koski-Homi](https://github.com/migetonni)
- [Miko Heino](https://github.com/Nakk1makkara)
