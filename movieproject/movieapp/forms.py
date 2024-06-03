from django import forms
from .models import Movie1

class Movie1Form(forms.ModelForm):
    class Meta:  # 'Meta' should be capitalized
        model = Movie1
        fields = ['name', 'desc', 'year', 'images']
