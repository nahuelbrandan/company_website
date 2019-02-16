from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Room(models.Model):
    id = models.AutoField(primary_key=True)
    # username = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, null=False)
    description = models.CharField(max_length=10000, null=False)
    price = models.IntegerField(null=False)
    principal_image = models.ImageField(upload_to='media', null=False)
    aditional_image = models.ImageField(upload_to='media', null=True)
    aditional_image_2 = models.ImageField(upload_to='media', null=True)
    aditional_image_3 = models.ImageField(upload_to='media', null=True)

    def __str__(self):
        return self.title
