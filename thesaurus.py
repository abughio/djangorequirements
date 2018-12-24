import os, django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_project.settings")
django.setup()

from nltk.corpus import wordnet
#from sets import Set

from dialogflow.models import Topic, Synonym

import inflect
plurals = inflect.engine()

from nltk.corpus import stopwords
stop = set(stopwords.words('english'))

results = Topic.objects.all()

for result in results:
    for word in result.name.split():

        if word in stop:
            continue

        synonyms = set()
        for syn in wordnet.synsets(word):

            if ".n." in str(syn):

                for l in syn.lemmas():
                    lemma = l.name()
                    if (lemma.isalpha()):
                        synonyms.add(lemma)
                        synonyms.add(plurals.plural(lemma))

            if ".a." in str(syn):
                synonyms = set()
                break

        print("{} , {}, {}".format(result.name, word, synonyms))

        # kind = 'Synonym'
        # synonym_key = datastore_client.key(kind, result.key.name)
        #
        # synonym = datastore.Entity(key=synonym_key)
        # synonym['synonym'] = result.key.name
        #
        # datastore_client.put(synonym)
        #
        # synonym_key = datastore_client.key(kind, word)

        # synonym = datastore.Entity(key=synonym_key)
        # synonym['synonym'] = result.key.name
        #
        # datastore_client.put(synonym)

        for dictionary_synonym in synonyms:
            s = Synonym()
            s.name = dictionary_synonym
            s.topicId = result
            s.save()

            print(dictionary_synonym)

            # synonym_key = datastore_client.key(kind, dictionary_synonym)
            #
            # synonym = datastore.Entity(key=synonym_key)
            # synonym['synonym'] = result.key.name
            #
            # datastore_client.put(synonym)

        # synonym_key = datastore_client.key(kind, plurals.plural(word))
        #
        # synonym = datastore.Entity(key=synonym_key)
        # synonym['synonym'] = result.key.name
        #
        # datastore_client.put(synonym)