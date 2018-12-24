from django.shortcuts import render
from django.views.generic import CreateView
from django.forms   import ModelForm
from .models import Comment

class CommentCreateView(ModelForm):
    class Meta:
        model = Comment
        fields = ['title', 'text']

    def form_valid(self, post):
        #print("Hello There")
        self.instance.postId = post
        self.instance.author = post.author
        return super().is_valid()


