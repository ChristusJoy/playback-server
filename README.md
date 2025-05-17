
# Flask Spotify Controller

A simple Flask web application to control Spotify playback via Spotify Web API.  
Users can authenticate with Spotify, then play, pause, skip tracks, and view current playback status.

---

## Features

- Spotify OAuth 2.0 authentication  
- Play/pause toggle  
- Skip to next or previous track  
- Display current playback information  

---

## Getting Started

### Prerequisites

- Python 3.7+  
- A Spotify Developer account with an app created  
- `pip` package manager  

---

### Setup

1. **Clone the repository**

```bash
git clone https://github.com/yourusername/spotify-controller.git
cd spotify-controller
```

2. **Create and activate a virtual environment**

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Create a `.env` file in the project root with the following variables**

```env
SPOTIPY_CLIENT_ID=your_spotify_client_id
SPOTIPY_CLIENT_SECRET=your_spotify_client_secret
SPOTIPY_REDIRECT_URI=http://localhost:5000/callback
```

> Replace the values with your actual Spotify app credentials and a random secret key for Flask sessions.

5. **Set the Redirect URI in your Spotify Developer Dashboard**

Make sure the Redirect URI matches the `SPOTIPY_REDIRECT_URI` in your `.env`. For local development, use:

```
http://localhost:5000/callback
```

---

### Running the app

```bash
flask run
```

Or, if you want to run with debug mode enabled:

```bash
python app.py
```

Open your browser and navigate to [http://localhost:5000](http://localhost:5000) to start.

---

## Deployment

- Use services like [Render](https://render.com) or [Railway](https://railway.app) to deploy this Flask app.
- Remember to set environment variables securely on your hosting platform.
- Update your Spotify Redirect URI to point to your deployed domain's `/callback` route.

---

## Notes

- Do **not** commit your `.env` file to version control.
- Use the `.env.example` file as a template for required environment variables.

---

## License

MIT License

---

## Acknowledgments

- [Spotify Web API](https://developer.spotify.com/documentation/web-api/)
- [Spotipy Python Library](https://spotipy.readthedocs.io/en/2.19.0/)
- Flask Framework

---

Feel free to open issues or submit pull requests!
