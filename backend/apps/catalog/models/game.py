from django.db import models

GENRE_LIST = [
    ('horror', 'Horror'),
    ('fps', 'FPS'),
    ('basquete', 'Basquete'),
    ('soccer', 'Soccer'),
    ('open_world', 'Open World'),
    ('third_person', 'Third Person'),
    ('rpg', 'RPG'),
    ('adventure', 'Adventure'),
    ('futball', 'Futball'),
]

class Game(models.Model):
    name = models.CharField(max_length=50)
    release_date = models.DateField()
    game_tag = models.CharField(max_length=7, db_index=True) 
    genre = models.CharField(max_length=20, choices=GENRE_LIST)
    publisher = models.CharField(max_length=50,  db_index=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='games/')  
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "catalog_game"
        ordering = ["-created_at"]

    def __str__(self):
        return self.name
