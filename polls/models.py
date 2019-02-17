from django.db import models
from django.forms import ModelForm
from django.conf import settings
from django.utils import timezone
# Create your models here.

class Suggestions(models.Model):
    name= models.CharField(max_length=200)
    suggestions_text= models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    def publish(self):
        self.published_date = timezone.now()
        self.save()
    def __str__(self):
        return self.name

