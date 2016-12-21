from basketball.models import Game
from basketball.bin.serializers import GameSerializer


class Handlers:
    def __init__(self):
        pass

    def get_game_list(self, request_object):
        games = Game.objects.all()
        game_serializer = GameSerializer(games, many=True)
        return game_serializer

    def post_game_list(self, request_object):
        game_serializer = GameSerializer(data=request_object)
        return game_serializer

    def get_game_detail(self, game):
        game_serializer = GameSerializer(game)
        return game_serializer

    def put_game_detail(self, game, request_object):
        game_serializer = GameSerializer(game, data=request_object)
        return game_serializer

