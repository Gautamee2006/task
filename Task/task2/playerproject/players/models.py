from django.db import models

class Player(models.Model):
    player_name = models.CharField(max_length=100)
    player_email = models.EmailField(unique=True)
    sports_name = models.CharField(max_length=100)
    coach_name = models.CharField(max_length=100)
    country_name = models.CharField(max_length=100)

    def __str__(self):
        return self.player_name
