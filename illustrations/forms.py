from django import forms
from .models import PostDoodle

class PostDoodleForm(forms.ModelForm):
    class Meta:
        model = PostDoodle
        fields = ['photo', 'text']