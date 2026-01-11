from django.urls import path
from .views import  *

urlpatterns = [
    path("home/", home, name="home"),
    path("movie_inside/<int:movie_id>/", movi_inside, name="movie_inside"),
    path("aloqa/", aloqaqilish, name="aloqa"),
    path("qoida/", qoida, name="qoida"),
    path("istoria/", istoria, name="istoria"),
    path("bar/", bar, name="bar"),
    path("music/", music, name="music"),
    path("game/", game, name="game"),
]
