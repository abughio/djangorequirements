import os, django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_project.settings")
django.setup()

from dialogflow.models import Topic

topics = Topic.objects.all()

for topic in topics:
    for c in topic.name:
        if c !='\n':
            print(c)