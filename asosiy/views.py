from django.shortcuts import render, get_object_or_404

from .models import Main_Movie
def base(request):
    return render(request, "base.html")


def home(request):
    kino = Main_Movie.objects.all()
    return render(request, "home.html", {"kino": kino})


def navigation(request):
    return render(request, "navigation.html")

def footer(request):
    return render(request, "footer.html")


def movi_inside(request, movie_id):
    kino = get_object_or_404(Main_Movie, id=(movie_id))
    return render(request, "movi_inside.html", {"kino": kino})

def aloqaqilish(request):
    return render(request, "aloqa.html")
def qoida(request):
    return render(request, "qoida.html")