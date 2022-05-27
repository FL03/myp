import random
import secrets

from ...data.structures import Token


def generate_token(a: int = 0, b: int = 32) -> Token:
    return Token(token=secrets.token_hex(b + random.randint(a, b)))
