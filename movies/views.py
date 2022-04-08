from django.views.decorators.http import require_http_methods
from django.shortcuts import get_object_or_404, redirect, render
from .models import Movie
from .forms import MovieForm

# Create your views here.
def index(request):
    movie_list = Movie.objects.order_by('-pk')
    context = {
        'movie_list': movie_list,
    }
    return render(request, 'movies/index.html', context)

@require_http_methods(['GET', 'POST'])
def create(request):
    if request.method == "POST":
        form = MovieForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('movies:index')
    else:
        form = MovieForm()
    context = {
        'form' : form
    }
    return render(request, 'movies/create.html', context)
