from django.conf.urls import url
from basketball import views

urlpatterns = [
    url(r'^basketball/games/?$', views.game_list),
    url(r'^basketball/games/(?P<pk>[0-9]+)/?$', views.game_detail),
    url(r'^basketball/game-locations/?$', views.game_locations),
    url(r'^basketball/game-locations/(?P<pk>[0-9]+)/?$', views.game_location_detail),
    url(r'^basketball/players/?$', views.player_list),
    url(r'^basketball/players/(?P<pk>[0-9]+)/?$', views.player_detail),
    url(r'^basketball/scores/?$', views.scores_list),
    url(r'^basketball/scores/(?P<pk>[0-9]+)/?$', views.score_detail),
]