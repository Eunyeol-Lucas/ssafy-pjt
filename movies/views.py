from django.shortcuts import redirect, render
import requests
from pprint import pprint
from .models import Movie


# Create your views here.

def index(request):
    movie_list = Movie.objects.all().order_by("-pk")
    context = {
        "movie_list": movie_list
    }
    return render(request, 'movies/index.html', context)

def new(request):
    return render(request, 'movies/new.html')

def create(request):
    title = request.POST.get("title")
    release_date = request.POST.get("release-date")
    poster_url = request.POST.get("poster-url")
    genre = request.POST.get("genre")
    description = request.POST.get("description")
    score = request.POST.get("score")
    audience = request.POST.get("audience")
    Movie.objects.create(
        title=title, release_date=release_date, poster_url=poster_url, genre=genre, description=description, score=score, audience=audience
    )
    return redirect("movies:index")

def detail(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    context = {
        "movie": movie
    }
    return render(request, "movies/detail.html", context)

def edit(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    context = {
        "movie": movie
    }
    return render(request, 'movies/edit.html', context)

def update(request, movie_id):
    title = request.POST.get("title")
    release_date = request.POST.get("release-date")
    poster_url = request.POST.get("poster-url")
    genre = request.POST.get("genre")
    description = request.POST.get("description")
    score = request.POST.get("score")
    audience = request.POST.get("audience")

    movie = Movie.objects.get(id=movie_id)
    movie.title=title
    movie.release_date=release_date
    movie.poster_url=poster_url
    movie.genre=genre
    movie.description=description
    movie.score=score
    movie.audience=audience

    movie.save()
    return redirect("movies:index")

def delete(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    movie.delete()
    return redirect('movies:index')

