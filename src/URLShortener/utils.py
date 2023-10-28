import secrets

import shortuuid
from passlib.context import CryptContext


def generate_short_url():
    return shortuuid.uuid()[:8]


def generate_unique_name(filename: str, short_url: str) -> str:
    return filename + short_url



