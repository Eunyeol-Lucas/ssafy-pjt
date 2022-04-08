from django.shortcuts import get_object_or_404, render
from .models import Movie

# Create your views here.
def index(request):
    movie_list = Movie.objects.order_by('-pk')
    context = {
        'movie_list': movie_list,
    }
    return render(request, 'movies/index.html', context)