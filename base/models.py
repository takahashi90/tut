from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE

# Create your models here.

class Topic(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Room(models.Model):
    # host = 
    topic = models.ForeignKey(Topic, on_delete = models.SET_NULL, null=True)
    name = models.CharField(max_length=200) # we have to specify the type of the model
    description = models.TextField(null=True, blank=True) # null being true means that description can be empty it is to give user choice to add description later or to never add one and blank = true means that when form is submitted, it could also be empty
    # participants =
    updated = models.DateTimeField(auto_now=True) # it would automatically take the time stamp whenever the table is updated aur when we run save method
    created = models.DateTimeField(auto_now_add=True) # difference between auto now and auto now add is that auto now takes time stamp each time we save and auto now add only takes at the time its created

    def __str__(self):
        return self.name

class Message(models.Model): # child model of Room
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    room = models.ForeignKey(Room, on_delete = models.CASCADE)
    body = models.TextField() # the message that user would write 
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return self.body[0:50] # it would show only first 50 chracters so if the message is long preview would show only 50 chracter part of it 
