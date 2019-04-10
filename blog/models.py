from django.db import models

class Post(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    id = models.AutoField(primary_key=True)

