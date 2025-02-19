from flask import Flask, jsonify, send_from_directory
import requests
from flask_cors import CORS
import time
import os

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Cache the price for 30 seconds
cache = {
    'price': None,
    'last_update': 0
}

CACHE_DURATION = 30  # seconds

@app.route('/api/bitcoin-price')
def get_bitcoin_price():
    current_time = time.time()
    print(f"Received price request at {current_time}")  # Debug log
    
    # Return cached price if it's less than 30 seconds old
    if cache['price'] and current_time - cache['last_update'] < CACHE_DURATION:
        print("Returning cached price:", cache['price'])  # Debug log
        return jsonify(cache['price'])
    
    try:
        print("Fetching new price from CoinGecko")  # Debug log
        response = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd')
        response.raise_for_status()  # Raise an error for bad status codes
        data = response.json()
        print("Received data from CoinGecko:", data)  # Debug log
        
        # Update cache
        cache['price'] = data
        cache['last_update'] = current_time
        
        return jsonify(data)
    except Exception as e:
        print(f"Error fetching price: {str(e)}")  # Debug log
        return jsonify({'error': str(e)}), 500

# Serve the overlay.html file at the root URL
@app.route('/')
def serve_overlay():
    return send_from_directory('.', 'overlay.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True) 