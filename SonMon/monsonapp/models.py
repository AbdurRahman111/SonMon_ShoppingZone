from django.db import models

# Create your models here.


class register(models.Model):
    name=models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    password=models.CharField(max_length=200)
    confirm_password=models.CharField(max_length=200)