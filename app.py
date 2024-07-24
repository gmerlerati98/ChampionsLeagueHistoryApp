from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

# Load the data
df = pd.read_csv('data/team_matches.csv')

@app.route('/')
def index():
    teams = sorted(set(df['home_team']).union(set(df['away_team'])))
    return render_template('index.html', teams=teams)

@app.route('/filter', methods=['POST'])
def filter():
    team = request.form.get('team')
    filtered_df = df[(df['home_team'] == team) | (df['away_team'] == team)]
    return render_template('index.html', tables=[filtered_df.to_html(classes='data', header="true")], teams=sorted(set(df['home_team']).union(set(df['away_team']))))

if __name__ == '__main__':
    app.run(debug=True)
