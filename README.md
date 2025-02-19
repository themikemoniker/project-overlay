# project-overlay
OBS overlay powered by lightning payments

## Setup Instructions

### 1. Start the Server
```bash
# Install dependencies (first time only)
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# Start the server
python server.py
```

### 2. Add to OBS
1. In OBS Studio, add a new "Browser Source" to your scene
2. **Important:** Ensure "Local file" is **unchecked**
3. Enter the overlay URL: `http://localhost:8080`
4. Set the recommended dimensions:
   - Width: 1920px
   - Height: 1080px
5. Click "OK" to add the overlay to your scene

## Development

The overlay is built using HTML, CSS, and JavaScript. The main files are:
- `overlay.html` - The main overlay file
- `server.py` - The server that hosts both the overlay and the Bitcoin price API

### Local Development
Just run the server and it will handle everything:
```bash
python server.py
```

### Production Hosting
For production use, you'll need to:
1. Host the Flask server on a reliable hosting service
2. Update the OBS browser source URL to point to your production server

Recommended hosting options:
- DigitalOcean
- Heroku
- AWS
- Your own VPS
