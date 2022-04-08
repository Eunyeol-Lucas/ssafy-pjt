from django import forms
from .models import Movie

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ('title', 'audience', 'release_date', 'genre', 'score', 'post_url', 'description')
    