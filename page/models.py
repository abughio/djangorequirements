from django.db import models

class Page(models.Model):
    title = models.CharField(max_length=300)
    summary = models.TextField()
    body = models.TextField()
    published = models.BooleanField()
    commentsAllowed = models.BooleanField()

    def __str__(self):
        return self.title