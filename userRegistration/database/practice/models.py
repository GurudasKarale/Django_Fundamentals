from django.db import models

class Forms(models.Model):

    name=models.CharField(max_length=100,null=True)
    email=models.CharField(max_length=100,null=True)
    password1=models.CharField(max_length=100,null=True)
