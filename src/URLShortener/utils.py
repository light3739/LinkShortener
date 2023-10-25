import secrets

import shortuuid
from passlib.context import CryptContext


def generate_short_url():
    return shortuuid.uuid()[:8]


def generate_unique_name(filename: str, short_url: str) -> str:
    return filename + short_url


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def generate_and_hash_password() -> str:
    password = secrets.token_urlsafe(16)  # Generate a random password
    return pwd_context.hash(password)  # Hash the password
