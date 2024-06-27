# backend/app/routes.py
import os
import requests
from flask import request, current_app as app

SPORTSDB_KEY = os.getenv('SPORTSDB_KEY')

# Fetch soccer games from multiple leagues using The Sports DB API
def fetch_soccer_games(season='2023-2024'):
    leagues = {
        'Premier League': '4328',
        'La Liga': '4335',
        'Major Soccer League': '4346',
        'Champions League': '4480',
        'Euros': '4502'
    }
    games = []

    for league, league_id in leagues.items():
        url = f'https://www.thesportsdb.com/api/v1/json/{SPORTSDB_KEY}/eventsseason.php?id={league_id}&s={season}'
        response = requests.get(url)
        # print(f"Fetching data for {league}: {url}")
        if response.status_code == 200:
            # print(f"Response status code: {response.status_code}")
            league_games = response.json().get('events', [])
            # print(f"Response JSON for {league}: {response.json()}")
            if league_games is not None:
                for game in league_games:
                    games.append({
                        'league': league,
                        'game': game
                    })
        else:
            print(f"Failed to fetch data for {league}: {response.status_code}")

    return games

# Route to get soccer games for the 2023-2024 season
@app.route('/', methods=['GET'])
def get_soccer_games():
    soccer_games = fetch_soccer_games()
    return soccer_games
