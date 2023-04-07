from django import forms
from .models import Post,Comment,Profile

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['image', 'video', 'caption']



class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields=['text']

class Profileform(forms.ModelForm):
    class Meta:
        model=Profile
        fields= ['profile_img']