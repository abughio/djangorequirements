from django.db import models


class Topic(models.Model):
    name = models.CharField(max_length=100)
    text = models.TextField(max_length=2000)

    def __str__(self):
        return self.name


class Synonym(models.Model):
    name = models.CharField(max_length=100)
    topicId = models.ForeignKey(Topic,on_delete=models.CASCADE,related_name="synonyms")

    def __str__(self):
        return self.name

