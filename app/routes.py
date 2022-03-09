from app import app
from flask import render_template

@app.route('/')
def home():
    return render_template('index.html')



@app.route('/Artists')
def faveartists():
    Artists = ['Kanye West', 'Trippie Redd', 'Anderson Pak', 'Snoh Aalegra','Gunna']
    return render_template('Artists.html', fave_artists = Artists)


@app.route ('/Games')
def favegames():
    Games = [ 'Valorant', 'Lost Ark', 'NBA2K', 'Call of Duty', 'Fifa']
    return render_template ('Games.html', fave_games = Games)