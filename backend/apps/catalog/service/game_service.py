from django.conf import settings
import os
from apps.catalog.models.game import Game
from apps.catalog.models.game_image import GameImage
from apps.catalog.utils.game_utils import generate_game_tag

class GameServiceCreate:
    @staticmethod
    def create_game(dto):
        if not dto.game_tag:
            dto.game_tag = generate_game_tag()
        game = Game.objects.create(
            name=dto.name,
            release_date=dto.release_date,
            genre=dto.genre,
            publisher=dto.publisher,
            price=dto.price,
            game_tag=dto.game_tag
        )
        game_dir = os.path.join(settings.MEDIA_ROOT, "games")
        os.makedirs(game_dir, exist_ok=True)
        for i, img_file in enumerate(dto.images[:3]):
            game_image = GameImage(game=game, is_cover=(i == 0))  
            game_image.image.save(img_file.name, img_file, save=True)

        return game
