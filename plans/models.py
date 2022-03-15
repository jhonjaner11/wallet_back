from django.db import models

class plans(models.Model):
    name = models.CharField( max_length=50)
    duration = models.IntegerField()
    min_deposit = models.IntegerField()
    max_deposit = models.IntegerField()
    percentage = models.FloatField()

    def __str__(self):
        return self.name
    