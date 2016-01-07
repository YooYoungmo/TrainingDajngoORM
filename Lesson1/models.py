from __future__ import unicode_literals
from django.db import models #1


class Person(models.Model): #2
    first_name = models.CharField(max_length=30) #3
    last_name = models.CharField(max_length=30) #4