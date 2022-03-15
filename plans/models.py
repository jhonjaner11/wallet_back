from django.db import models
from django.forms import IntegerField
from django.contrib.auth.models import User

class plans(models.Model):
    name = models.CharField( max_length=50)
    duration = models.IntegerField()
    min_deposit = models.IntegerField()
    max_deposit = models.IntegerField()
    percentage = models.FloatField()

    def __str__(self):
        return self.name
    
class subscription(models.Model):
    
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    plan = models.ForeignKey(plans, on_delete=models.CASCADE)
    date = models.DateTimeField()

    def __str__(self):
        return str(self.id)
