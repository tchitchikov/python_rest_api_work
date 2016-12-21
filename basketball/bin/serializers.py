from rest_framework import serializers
from basketball.models import Game


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ('id', 'name', 'event_date', 'game_description', 'completed')
