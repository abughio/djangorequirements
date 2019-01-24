import os, django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_project.settings")
django.setup()

from dialogflow.models import Topic

employee_handbook = open('book.txt', 'r')
while True:

    topic = employee_handbook.readline()
    if not (topic):
        break

    if (topic != '\r\n') and (len(topic.split(' ')) < 5):

        action_text = ''

        last_line = ''
        line = employee_handbook.readline()

        while (last_line != '\r\n') and (line != '\r\n') and (len(line.split(' ')) > 5):
            action_text += line
            last_line = line
            line = employee_handbook.readline()

        if action_text != '':

            t = Topic()
            t.name = topic
            t.text = action_text
            t.save()




            print('saved {}: {}'.format(topic, action_text))