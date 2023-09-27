from django.db import models
from django.contrib.auth.models import User

class Contact(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    logo = models.FileField(upload_to="images")
    def __str__(self):
        return self.user.username
   

class Group(models.Model):
    name = models.CharField(max_length=50)
    contacts = models.ManyToManyField(Contact, related_name='groups', blank=True)

    def __str__(self):
        return self.name
