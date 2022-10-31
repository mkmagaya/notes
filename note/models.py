from cgitb import text
from statistics import mode
from django.db import models

class Note(models.Model):
    title = models.CharField(max_length=100)
    notes = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
