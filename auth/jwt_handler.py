import time
from typing import Dict

import jwt

from config.config import Settings


def token_response(token: str, refresh_token:str, email: str, name: str, id: str):
    return {id: "id", "email": email, "name": name,"accessToken": token,"refreshToken": refresh_token}

def refresh_token_response(token: str, email: str, name: str):
    return {"email": email, "name": name,"refreshToken": token}

secret_key = Settings().secret_key


def sign_jwt(user_id: str, name: str, id: str) -> Dict[str, str]:
    # Set the expiry time.
    payload = {"user_id": user_id, "expires": time.time() + 2400}
    refresh_jwt = {"user_id": user_id, "expires": time.time() + 2600}
    token = jwt.encode(payload, secret_key, algorithm="HS256")
    refresh_token = jwt.encode(refresh_jwt, secret_key, algorithm="HS256")
    return token_response(token, refresh_token , user_id, name, id)

def refresh_jwt(user_id: str, name: str) -> Dict[str, str]:
    # Set the expiry refresh time.
    payload = {"user_id": user_id, "expires": time.time() + 2400}
    return refresh_token_response(jwt.encode(payload, secret_key, algorithm="HS256"), user_id, name)


def decode_jwt(token: str) -> dict:
    decoded_token = jwt.decode(token.encode(), secret_key, algorithms=["HS256"])
    return decoded_token if decoded_token["expires"] >= time.time() else {}
