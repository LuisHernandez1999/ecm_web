from dataclasses import dataclass
from decimal import Decimal
from typing import List
from django.core.files.uploadedfile import UploadedFile
@dataclass
class CreateGameDTO:
    def __init__(self, name, release_date, genre, publisher, price, images=None, game_tag=None):
        self.name = name
        self.release_date = release_date
        self.genre = genre
        self.publisher = publisher
        self.price = price
        self.images = images or []  
        self.game_tag = game_tag
        
@dataclass
class GameResponseDTO:
    id: int
    name: str
    release_date: str
    game_tag: str
    genre: str
    publisher: str
    price: Decimal
    images: list[str]  
