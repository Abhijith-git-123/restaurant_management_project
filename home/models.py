from django.db import models

# Create your models here.

class Restaurant(models.Model):
    name = models.CharField(max_length = 200)
    phone = models.CharField(max_length=30)
    email = models.CharField(max_length=50)


    def _str__(self):
        return self.name



class feedback(models.Model):
    comment = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.submitted_at