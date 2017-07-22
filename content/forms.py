from django import forms
from .models import Post
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text',)

class PostForm1(forms.Form):
    title   = forms.CharField()
    text    = forms.CharField()

