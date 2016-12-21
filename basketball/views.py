from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from basketball.bin.handlers import Handlers
from basketball.models import Game


@api_view(['GET', 'POST'])
@csrf_exempt
def game_list(request):
    handler = Handlers()
    if request.method == 'GET':
        games_serializer = handler.get_game_list(request.data)
        return Response(games_serializer.data)
    elif request.method == 'POST':
        game_serializer = handler.post_game_list(request.data)
        if game_serializer.is_valid():
            game_serializer.save()
            return Response(game_serializer.data, status=status.HTTP_201_CREATED)
        return Response(game_serializer.errors, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET', 'PUT', 'DELETE'])
@csrf_exempt
def game_detail(request, pk):
    try:
        game = Game.objects.get(pk=pk)
    except Game.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    handler = Handlers()

    if request.method == 'GET':
        game_serializer = handler.get_game_detail(game)
        return Response(game_serializer.data)
    elif request.method == 'PUT':
        game_serializer = handler.put_game_detail(game, request.data)
        if game_serializer.is_valid():
            game_serializer.save()
            return NResponse(game_serializer.data, status=status.HTTP_201_CREATED)
        return Response(game_serializer.errors, status=status.HTTP_404_NOT_FOUND)
    elif request.method == 'DELETE':
        game.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
