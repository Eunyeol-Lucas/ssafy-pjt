from django.shortcuts import render
from .models import Movie
# Create your views here.
def index(request):
    movies = Movie.objects.order_by('-pk')
    context = {
        'movies':movies,
    }
    return render(request,'movies/index.html',context)