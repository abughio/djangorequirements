from django.contrib import admin
from . import models

admin.site.register(models.Post)
admin.site.register(models.Questionnaire)
admin.site.register(models.Item)
admin.site.register(models.Scale)
admin.site.register(models.Score)

