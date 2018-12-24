from django.db import models
from django.utils import timezone
from polymorphic.models import PolymorphicModel


class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Project(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=500, default=' - ')
    client_name = models.CharField(max_length=200)
    expected_start = models.DateTimeField(default=timezone.now)
    expected_finish = models.DateTimeField(default=timezone.now)
    category = models.ForeignKey(Category, on_delete=None)

    def __str__(self):
        return self.name


class Animal(PolymorphicModel):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Cat(Animal):
    family = models.CharField(max_length=200)



class Dog(Animal):
    breed = models.CharField(max_length=200)



class Fights(models.Model):
    location = models.CharField(max_length=200)
    winner = models.ForeignKey(Animal,on_delete=models.CASCADE,related_name="victories")
    looser = models.ForeignKey(Animal,on_delete=models.CASCADE,related_name="defeats")

    def __str__(self):
        return self.winner.name+" defeats "+self.looser.name+" at "+self.location