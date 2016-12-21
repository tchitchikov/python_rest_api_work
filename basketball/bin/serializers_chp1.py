from rest_framework import serializers
from basketball.models import Game

class GameSerializer(serializers.Serializer):
    pk = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=200)
    event_date = serializers.DateTimeField()
    game_description = serializers.CharField(max_length=500)
    completed = serializers.BooleanField(required=False)

    def create(self, validated_data):
        return Game.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.event_date = validated_data.get('event_date', instance.event_date)
        instance.game_description = validated_data.get(
            'game_description', instance.game_description)
        instance.completed = validated_data.get('completed', instance.completed)
        instance.save()
        return instance
