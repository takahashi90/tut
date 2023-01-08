from django.db import models

# Create your models here.

class Room(models.Model):
    # host = 
    # topic =
    name = models.CharField(max_length=200) # we have to specify the type of the model
    description = models.TextField(null=True, blank=True) # null being true means that description can be empty it is to give user choice to add description later or to never add one and blank = true means that when form is submitted, it could also be empty
    # participants =
    updated = models.DateTimeField(auto_now=True) # it would automatically take the time stamp whenever the table is updated aur when we run save method
    created = models.DateTimeField(auto_now_add=True) # difference between auto now and auto now add is that auto now takes time stamp each time we save and auto now add only takes at the time its created

    def __str__(self):
        return self.name