# apps/catalog/models/game_image.py
from django.db import models
from apps.catalog.models.game import Game

class GameImage(models.Model):
    game = models.ForeignKey(Game, related_name="images", on_delete=models.CASCADE)
    image = models.ImageField(upload_to="games/")
    is_cover = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.game.name} Image"
