from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.fields import GenericRelation
from polymorphic.models import PolymorphicModel
from django.contrib.auth.models import User

class Artifact(PolymorphicModel):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class RequirementType(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Requirement(Artifact):
    type = models.ForeignKey(RequirementType,on_delete=models.CASCADE)
    desc = models.TextField()

    def __str__(self):
        return self.type+"-"+self.desc

class Story(Artifact):
    desc = models.TextField
    points = models.PositiveIntegerField


class BusinessRule(Artifact):
    desc = models.TextField

class Actor(Artifact):
    type = models.CharField(max_length=200, choices=[("Human","Human"),("System","System")])


class Usecase(Artifact):
    description = models.TextField(max_length=2000, blank=True)
    preConditions = models.TextField(max_length=2000,blank=True)
    postConditions = models.TextField(max_length=2000,blank=True)
    trigger = models.TextField(max_length=2000,blank=True)
    includes = models.ForeignKey("self",on_delete=None,related_name="extended_by",blank=True)
    extendes = models.ForeignKey("self",on_delete=None,related_name="included_by",blank=True)
    businessRules = models.ManyToManyField(BusinessRule)
    requirements = models.ManyToManyField(Requirement)

class Scenario(models.Model):
    SCENARIO_TYPES = (
        ('Normal','Normal'),
        ('Alternate','Alternate'),
        ('Exception','Exception')
    )
    entryPoint = models.CharField(max_length=20)
    desc = models.TextField(max_length=1000)
    type = models.CharField(max_length=200,choices=SCENARIO_TYPES)
    usecase = models.ForeignKey(Usecase,on_delete=models.CASCADE,related_name="scenarios")

    def __str__(self):
        return self.type.__str__()+" "+self.entryPoint.__str__()+" - "+self.desc.__str__()

class Step(models.Model):
    stepNo = models.IntegerField()
    desc = models.CharField(max_length=1000)
    uses = models.CharField(blank=True,max_length=100)
    state = models.CharField(blank=True,max_length=100)
    scenario = models.ForeignKey(Scenario,on_delete=models.CASCADE,related_name="steps")

    class meta:
        ordering = ['stepNo']

    def __str__(self):
        return self.stepNo.__str__()+" - "+self.desc.__str__()

class UsecaseActors(models.Model):
    actors = models.ForeignKey(Actor,models.CASCADE,related_name="usecases")
    usecases = models.ForeignKey(Usecase,models.CASCADE,related_name="actors")

class MessageType(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name



class Datamodel(Artifact):
    desc = models.TextField

Types = [("Numeric", "Numeric"),
         ("AlphaNumeric","AlphaNumeric"),
         ( "Boolean","Boolean" ),
         ("Date","Date" ),
         ("Button/Link","Button/Link")
         ]
Uniqueness = [("Mandatory", "Mandatory"),
              ("Optional", "Optional"),
              ("Conditional","Conditional")
              ]
class Field(models.Model):
    en = models.CharField(max_length=100)
    ar = models.CharField(max_length=100)
    min = models.PositiveIntegerField
    max = models.PositiveIntegerField
    type = models.CharField(max_length=100, choices=Types)
    unique = models.CharField(max_length=100,choices=Uniqueness)
    validations = models.TextField(null=True)
    Comments = models.TextField(null=True)
    entity = models.ForeignKey(Datamodel,on_delete=models.CASCADE,related_name="fields")




class LinkTypes(models.Model):
    name = models.CharField(max_length=100)
    reverse_name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


#Give your model a ForeignKey to ContentType. The usual name for this field is “content_type”.

#Give your model a field that can store primary key values from the models you’ll be relating to. For most models, \
# this means a PositiveIntegerField. The usual name for this field is “object_id”.

#Give your model a GenericForeignKey, and pass it the names of the two fields described above. If these fields are \
# named “content_type” and “object_id”, you can omit this – those are the default field names GenericForeignKey will \
# look for.
# class Link(models.Model):
#     source_content_type = models.ForeignKey(ContentType,on_delete=models.CASCADE,related_name="source")
#     target_content_type = models.ForeignKey(ContentType,on_delete=models.CASCADE,related_name="target")
#     source_object_id = models.PositiveIntegerField()
#     target_object_id = models.PositiveIntegerField()
#     source = GenericForeignKey('source_content_type','source_object_id')
#     target = GenericForeignKey('target_content_type','target_object_id')
#     link = models.ForeignKey(LinkTypes,on_delete=models.CASCADE)
#
#     def __str__(self):
#         return self.source.__str__()

class Message(Artifact):
    type = models.ForeignKey(MessageType,on_delete=models.CASCADE,related_name="messages")
    message_en = models.TextField()
    message_ar = models.TextField()


    def __str__(self):
        return self.type.name+" - "+self.message_en

class Link(models.Model):
    source = models.ForeignKey(Artifact,on_delete=None,related_name="soruce_links")
    target = models.ForeignKey(Artifact,on_delete=None,related_name="targets")
    linkType = models.ForeignKey(LinkTypes,on_delete=models.CASCADE,related_name="links")