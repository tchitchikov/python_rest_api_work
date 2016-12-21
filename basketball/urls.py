from django.conf.urls import url
from basketball import views

urlpatterns = [
    url(r'^basketball/?$', views.game_list),
    url(r'^basketball/(?P<pk>[0-9]+)/?$', views.game_detail),
]