from django.core.management.base import BaseCommand
from dialogflow.models import Topic

class Command(BaseCommand):
    def handle(self, **options):
        for n in Topic().objects.all():
            print(n.name)

        print("HelloWorld!")