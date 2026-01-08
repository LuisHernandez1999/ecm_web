from decimal import Decimal
from apps.catalog.models.game import GENRE_LIST
import random
import string
from django.utils.text import slugify
from apps.catalog.exceptions.game_exceptios import InvalidPrice, GenreNotAllowed

def validate_price(price: Decimal):
    if price <= Decimal("0"):
        raise InvalidPrice("Preço deve ser maior que zero")

def validate_genre(genre: str):
    allowed_genres = [g[0] for g in GENRE_LIST]
    if genre not in allowed_genres:
        raise GenreNotAllowed(f"Gênero '{genre}' não permitido")


def generate_slug(text: str) -> str:
    return slugify(text)

def generate_game_tag(length: int = 6) -> str:
    """Gera uma tag única: A1B2C3"""
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))