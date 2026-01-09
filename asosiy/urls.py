from django.urls import path
from .views import  *

urlpatterns = [
    path("home/", home, name="home"),
    path("movie_inside/<int:movie_id>/", movi_inside, name="movie_inside"),
    path("aloqa/", aloqaqilish, name="aloqa"),
    path("qoida/", qoida, name="qoida"),
]
