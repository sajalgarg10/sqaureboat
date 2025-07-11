from django.db import models
from users.models import User


# Create your models here.

class Jobs(models.Model):
    title = models.CharField(null = False , unique= True , max_length=256 )
    description = models.TextField(null = True)



class Applications(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    job = models.ForeignKey(Jobs , on_delete= models.CASCADE)
    




