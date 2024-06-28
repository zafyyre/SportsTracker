# backend/app/routes.py
import os
import requests
from flask import request, current_app as app

API_KEY = os.getenv('API_KEY')

def fetch_api_games(league_id):
    season = '2023-2024'
    url = f'https://www.thesportsdb.com/api/v1/json/{API_KEY}/eventsseason.php?id={league_id}&s={season}'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json().get('events', [])
    else:
        print(f"Failed to fetch data: {response.status_code}")
        return []

# Route to get Premier League games
@app.route('/soccer/premier-league', methods=['GET'])
def get_premier_league_games():
    games = fetch_api_games('4328')
    return games

# Route to get La Liga games
@app.route('/soccer/la-liga', methods=['GET'])
def get_la_liga_games():
    games = fetch_api_games('4335')
    return games

# Route to get Champions League games
@app.route('/soccer/champions-league', methods=['GET'])
def get_champions_league_games():
    games = fetch_api_games('4480')
    return games

# Basketball routes
@app.route('/basketball/nba', methods=['GET'])
def get_nba_games():
    games = fetch_api_games('4387')  # NBA
    return games

# Hockey routes
@app.route('/hockey/nhl', methods=['GET'])
def get_nhl_games():
    games = fetch_api_games('4380')  # NHL
    return games

