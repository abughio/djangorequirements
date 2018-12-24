from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length=100)
    summary = models.TextField(max_length=500,default=' - ')
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

class Questionnaire(models.Model):
    text = models.CharField(max_length=500)
    description = models.TextField()

    def __str__(self):
        return self.text


class Item(models.Model):
    text = models.CharField(max_length=500)
    parent = models.ForeignKey(Questionnaire,on_delete=models.CASCADE,related_name="items")

    def __str__(self):
        return self.text

class Scale(models.Model):
    name = models.CharField(max_length=200)
    lower = models.IntegerField()
    upper = models.IntegerField()
    parent = models.ForeignKey(Questionnaire,on_delete=models.CASCADE,related_name="scale")

    def __str__(self):
        return self.name

class Score(models.Model):
    score = models.IntegerField()
    Itemscored = models.ForeignKey(Item,on_delete=models.CASCADE,related_name="answer")

