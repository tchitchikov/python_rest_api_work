from django.db import models

# Create your models here.
class Game(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=200, default='', blank=True)
    event_date = models.DateTimeField()
    game_description = models.CharField(max_length=500, default='', blank=True)
    completed = models.BooleanField(default=True)


    class Meta:
        ordering = ('name', )
