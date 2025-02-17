from flask import Flask, jsonify, request
import jwt
import datetime
import uuid
from keys import generate_key, get_public_keys, get_private_key

app = Flask(__name__)

# Generate initial keys
keys = {}
kid, private_key, public_key, expiry = generate_key()
keys[kid] = {
    'private_key': private_key,
    'public_key': public_key,
    'expiry': expiry
}

# JWKS endpoint
@app.route('/jwks', methods=['GET'])
def jwks():
    jwks_keys = get_public_keys(keys)
    return jsonify({'keys': jwks_keys})

# Auth endpoint
@app.route('/auth', methods=['POST'])
def auth():
    expired = 'expired' in request.args
    kid = list(keys.keys())[0]  # Simplification for this example
    private_key = get_private_key(kid, keys)
    expiry = keys[kid]['expiry'] if not expired else datetime.datetime.utcnow() - datetime.timedelta(days=1)

    token = jwt.encode({'sub': 'user123', 'exp': expiry, 'kid': kid}, private_key, algorithm='RS256')
    return jsonify({'token': token})

if __name__ == '__main__':
    app.run(port=8080)
