from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.Project)
admin.site.register(models.Category)
admin.site.register(models.Animal)
admin.site.register(models.Cat)
admin.site.register(models.Dog)
admin.site.register(models.Fights)