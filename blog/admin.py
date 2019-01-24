from django.contrib import admin
from . import models

#admin.site.register(models.Post)
admin.site.register(models.Questionnaire)
admin.site.register(models.Item)
admin.site.register(models.Scale)
admin.site.register(models.Score)

@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title','summary','date_posted','author')
    list_filter = ('date_posted', 'author')
    search_fields = ('title', 'content')
    #prepopulated_fields = {'slug': ('title',)}
    #raw_id_fields = ('author',)
    #date_hierarchy = 'publish'
    #ordering = ('-date_posted')