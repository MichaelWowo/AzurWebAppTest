from django.db import models

# Create your models here.
class DidConfiguration(models.Model):
    @context = models.CharField(max_length=200, default='0000000', editable=False)

