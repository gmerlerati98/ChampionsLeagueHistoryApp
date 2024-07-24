import requests
import pandas as pd

API_KEY = '1c5c20d9b6e943efb02e464c938325d0'
URI = 'https://api.football-data.org/v4/competitions/CL/matches'
HEADERS = { 'X-Auth-Token': API_KEY }

def fetch_and_save_matches():
    response = requests.get(URI, headers=HEADERS)
    matches = []

    for match in response.json()['matches']:
        home_team = match['homeTeam']['name']
        away_team = match['awayTeam']['name']
        score = match['score']['fullTime']
        matches.append({
            'date': match['utcDate'],
            'home_team': home_team,
            'away_team': away_team,
            'score': score
        })
      
    df = pd.DataFrame(matches)
    df.to_csv('data/team_matches.csv', index=False)
    print("Data collected and saved to data/team_matches.csv")

if __name__ == "__main__":
    fetch_and_save_matches()

  