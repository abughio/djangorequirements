from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from blog.models import Post
from django.urls import reverse

class Comment(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField(max_length=500)
    postId = models.ForeignKey(Post,on_delete=models.CASCADE, default=None, related_name='comments')
    parentId = models.ForeignKey("self",on_delete=None,null=True, related_name='replies')
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User,on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.title

