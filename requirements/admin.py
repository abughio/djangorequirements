from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.RequirementType)
admin.site.register(models.Requirement)
admin.site.register(models.BusinessRule)
admin.site.register(models.Story)
admin.site.register(models.MessageType)
admin.site.register(models.Message)
admin.site.register(models.Usecase)
admin.site.register(models.LinkTypes)
admin.site.register(models.Link)
admin.site.register(models.Datamodel)
admin.site.register(models.Field)
admin.site.register(models.Scenario)
admin.site.register(models.Step)