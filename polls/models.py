from django.db import models
from django.forms import ModelForm
from django.conf import settings
# Create your models here.

class Suggestions(models.Model):
    name= models.CharField(max_length=200)
    suggestions_text= models.TextField()

