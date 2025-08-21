from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete = moels.CASCADE, related_name = "profile")


    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return self.name





class Restaurant(models.Model):
    name = models.CharField(max_length = 200)
    phone = models.CharField(max_length=30)
    email = models.CharField(max_length=50)
    address = models.TextField()
    opening_hours = models.JSONField(default = dict, blank=True)
    logo = models.ImageField(upload_to = 'restaurant_logos/',blank=True,null=True)


    def _str__(self):
        return self.name



class feedback(models.Model):
    comment = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.submitted_at


class contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return f"{self.name} - {self.email}"


class RestaurantLocation(models.Model):
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.address}, {self.city}, {self.state} - {self.zip_code}"