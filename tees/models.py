from django.db import models
from django.contrib.auth.models import User

class Shirt(models.Model):
	name = models.CharField(max_length=100)
	picture = models.ImageField(upload_to='tees')

class UserProfile(models.Model):
	user = models.ForeignKey(User, unique=True)
	shirt = models.ForeignKey(Shirt)
