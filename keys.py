import datetime
import uuid
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization

def generate_rsa_key():
    private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    public_key = private_key.public_key()
    return private_key, public_key

def generate_key():
    kid = str(uuid.uuid4())
    private_key, public_key = generate_rsa_key()
    expiry = datetime.datetime.utcnow() + datetime.timedelta(days=7)
    return kid, private_key, public_key, expiry

def get_public_keys(keys):
    jwks_keys = []
    for kid, key in keys.items():
        if key['expiry'] > datetime.datetime.utcnow():
            public_key_pem = key['public_key'].public_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PublicFormat.SubjectPublicKeyInfo
            ).decode('utf-8')
            jwks_keys.append({
                'kid': kid,
                'kty': 'RSA',
                'use': 'sig',
                'alg': 'RS256',
                'n': public_key_pem
            })
    return jwks_keys

def get_private_key(kid, keys):
    return keys[kid]['private_key']
