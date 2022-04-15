from re import L
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods, require_POST, require_safe
from movies.forms import CommentForm, MovieForm
from .models import Movie, Comment
# Create your views here.
def index(request):
    movies = Movie.objects.order_by('-pk')
    context = {
        'movies':movies,
    }
    return render(request,'movies/index.html',context)

def create(request):
    if request.method == "POST":
        form = MovieForm(request.POST)
        if form.is_valid():
            movie = form.save(commit=False)
            movie.user = request.user
            movie.save()
            return redirect('movies:index')
    else:
        form = MovieForm()
    context = {
        'form': form
    }

    return render(request, 'movies/create.html', context)

def detail(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    comment_form = CommentForm()
    comments = movie.comment_set.all()
    context  = {
        'movie': movie,
        'comment_form': comment_form,
        'comments': comments,
        'user': request.user.id
    }
    return render(request, 'movies/detail.html', context)

@login_required
@require_http_methods(['GET', 'POST'])
def update(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    if request.user.id == movie.user.id:
        if request.method == 'POST':
            form = MovieForm(request.POST, instance=movie)
            if form.is_valid():
                form.save()
                return redirect('movies:detail', movie.pk)
        else:
            form = MovieForm(instance=movie)
    else:
        return redirect('movies:index')
    context = {
        'movie': movie,
        'form': form
    }
    return render(request, 'movies/update.html', context)