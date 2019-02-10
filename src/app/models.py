from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Room(models.Model):
    id = models.AutoField(primary_key=True)
    # username = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, null=False)
    description = models.CharField(max_length=1000, null=False)
    address = models.CharField(max_length=100, null=False)
    image = models.ImageField(upload_to='media', null=False)

    def __str__(self):
        return self.title
