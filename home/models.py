from django.db import models

# Create your models here.

class Restaurant(models.Model):
    name = models.CharField(max_length = 200)


    def _str__(self):
        return self.name