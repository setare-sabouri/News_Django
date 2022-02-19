from django import forms
from . import models


class Create_News(forms.ModelForm):
    class Meta:
        model=models.News   #ersbari az new 
        fields=['title','slug','body','image']