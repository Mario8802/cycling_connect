from django import forms
from .models import BikePost


class BikePostForm(forms.ModelForm):
    class Meta:
        model = BikePost
        fields = ['title', 'description', 'price', 'image']