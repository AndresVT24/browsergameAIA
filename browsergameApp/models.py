from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class userRols(models.Model):
    idUser= models.ForeignKey(User, on_delete=models.CASCADE)
    rold= models.ImageField()

class players:
    name= models.ForeignKey(User.name)