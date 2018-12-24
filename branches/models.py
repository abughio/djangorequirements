from django.db import models
from django.core.validators import ValidationError
from django.contrib.auth.models import User
import re

# Create your models here.
class Region(models.Model):
    name = models.CharField(max_length=200)
    nameAR = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField(max_length=200)
    nameAR = models.CharField(max_length=200)
    region = models.ForeignKey(Region,on_delete=models.CASCADE,related_name="cities")

    def __str__(self):
        return self.name


class Branch(models.Model):
    crmainid = models.PositiveIntegerField
    crbranchid = models.PositiveIntegerField
    crexpiry = models.DateField
    retailerMainName = models.CharField(max_length=255)
    retailerNameEN  = models.CharField(max_length=200)
    retailerNameAR = models.CharField(max_length=200)
    region = models.ForeignKey(Region,on_delete=None,related_name="branches")
    city = models.ForeignKey(City,on_delete=None,related_name="branches")
    iban = models.CharField(max_length=25)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="branch", blank=True, default=None)

    def __str__(self):
        return self.retailerMainName+" -  "+self.retailerNameAR