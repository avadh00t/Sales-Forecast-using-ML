from django.db import models

# Create your models here.
    
class userinput(models.Model):
    retailer = models.CharField(max_length=45, default=None)
    region = models.CharField(max_length=45, default=None)
    state = models.CharField(max_length=45, default=None)
    city = models.CharField(max_length=45, default=None)
    product = models.CharField(max_length=45, default=None)
    method = models.CharField(max_length=45, default=None)
    priceperunit = models.IntegerField()
    unitssold = models.IntegerField()
    operatingprofit = models.IntegerField()
    operatingmargin = models.IntegerField()
    