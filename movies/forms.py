from platform import release
from tkinter import Widget
from turtle import width
from django import forms
from .models import Movie

class MovieForm(forms.ModelForm):
    GENRE_A = '코미디'
    GENRE_B = '공포'
    GENRE_C = '로맨스'
    GENRE_CHOICES = [
        (GENRE_A, '코미디'),
        (GENRE_B, '공포'),
        (GENRE_C, '로맨스'),
    ]
    
    title = forms.CharField(
        label="Title",
        widget=forms.TextInput(
            attrs={
                'placeholder': "Title",
                "class":"form-control" 
            }
        ),
    )
    audience = forms.IntegerField(
        label="Audience",
        widget=forms.NumberInput(
            attrs={
                'placeholder': 'audience',
                "class":"form-control" 
            }
        )
    )
    release_date = forms.DateTimeField(
        label="Release_date",
        widget=forms.DateInput(
            attrs={
                'type':'date',
                "class":"form-control" 
            }
        )
    )
    genre = forms.ChoiceField(
        label="Genre",
        choices=GENRE_CHOICES,
        widget=forms.Select(
            attrs={
                "class":"form-control" 
            }
        )
    )
    score = forms.IntegerField(
        label="Score",
        widget=forms.NumberInput(
            attrs={
                'type': 'number',
                'placeholder': 'Score',
                "class":"form-control" ,
                'max': 5,
                'min': 0.5,
                'step':0.5,
            }
        )
    )
    poster_url = forms.CharField(
        label="Poster url",
        widget = forms.TextInput(
            attrs={
                'placeholder':'Poster url',
                "class":"form-control" ,
            }
        )
    )
    description = forms.CharField(
        label="Description",
        widget=forms.Textarea(
            attrs={
                'placeholder':'Description',
                "class":"form-control" 
            }
        )
    )
    
    class Meta:
        model = Movie
        fields = ('title', 'audience', 'release_date', 'genre', 'score', 'poster_url', 'description')

    