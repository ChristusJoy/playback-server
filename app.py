from flask import Flask, redirect, request, jsonify, session
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
import os
from flask_cors import CORS
load_dotenv()

app = Flask(__name__)
CORS(app)

sp_oauth = SpotifyOAuth(
    client_id=os.getenv("SPOTIPY_CLIENT_ID"),
    client_secret=os.getenv("SPOTIPY_CLIENT_SECRET"),
    redirect_uri=os.getenv("SPOTIPY_REDIRECT_URI"),
    scope='user-modify-playback-state user-read-playback-state'
)

@app.route('/')
def index():
    auth_url = sp_oauth.get_authorize_url()
    return redirect(auth_url)

@app.route('/callback')
def callback():
    token_info = sp_oauth.get_access_token(request.args['code'])
    access_token = token_info['access_token']
    sp = spotipy.Spotify(auth=access_token)
    return "Authenticated! You can now control Spotify."

@app.route('/playpause', methods=['POST'])
def playpause():
    sp = spotipy.Spotify(auth_manager=sp_oauth)  
    playback = sp.current_playback()
    
    if playback and playback['is_playing']:
        sp.pause_playback()
    else:
        sp.start_playback()
    return jsonify(success=True)

@app.route('/next', methods=['POST'])
def next():
    sp = spotipy.Spotify(auth_manager=sp_oauth)
    sp.next_track()
    return jsonify(success=True)

@app.route('/previous', methods=['POST'])
def previous():
    sp = spotipy.Spotify(auth_manager=sp_oauth)
    sp.previous_track()
    return jsonify(success=True)

@app.route('/playback', methods=['GET'])
def playback():
    sp = spotipy.Spotify(auth_manager=sp_oauth)
    playback = sp.current_playback()
    if playback:
        return jsonify(playback)
    else:
        return jsonify(error="No active playback"), 404
    
    
if __name__ == '__main__':
    app.run(debug=True)
