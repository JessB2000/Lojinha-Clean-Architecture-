import os
from datetime import datetime, timedelta
from jose import jwt
from dotenv import load_dotenv

load_dotenv("vars.env")


def create_access_token(data: dict, expires_delta: timedelta = timedelta(
        minutes=int(os.getenv('ACCESS_TOKEN_EXPIRE_MINUTES')))):
    to_encode = data.copy()
    expire = datetime.utcnow() + expires_delta
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, os.getenv(
        'SECRET_KEY'), algorithm=os.getenv('ALGORITHM'))
    return encoded_jwt
