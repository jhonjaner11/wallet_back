from tokenize import Double
from django.db import models

# Create your models here.
from django.forms import IntegerField
from django.contrib.auth.models import User
from plans.models import plans

class reward(models.Model):
    adquisition_date = models.DateTimeField( )
    reddemed_date = models.DateTimeField()
    percentage = models.IntegerField()
    type = models.IntegerField()
    reffered_id = models.ForeignKey(User, related_name='reffered_id', on_delete=models.CASCADE)
    user_id =  models.ForeignKey(User,  related_name='user_id', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)
    
class transaction(models.Model):
    
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    plan = models.ForeignKey(plans, on_delete=models.CASCADE)
    date = models.DateTimeField()
    type = models.IntegerField()
    ammount = models.DecimalField(max_digits=10 ,decimal_places=2)
    date = models.DateTimeField()
    wallet_from = models.CharField( max_length=50)
    wallet_to = models.CharField( max_length=50)
    is_approved = models.BooleanField()
    approved_by = models.ForeignKey(User,  related_name='approved_by', on_delete=models.CASCADE)
    approved_date = models.DateTimeField()
    reward_id = models.ForeignKey(reward, on_delete=models.CASCADE)
    url_photo_proof = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return str(self.id)
