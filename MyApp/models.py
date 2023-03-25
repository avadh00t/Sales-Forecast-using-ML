from django.db import models

# Create your models here.
    
class userinput(models.Model):
    retailer = models.CharField(max_length=45)
    region = models.CharField(max_length=45)
    state = models.CharField(max_length=45)
    city = models.CharField(max_length=45)
    product = models.CharField(max_length=45)
    method = models.CharField(max_length=45)
    priceperunit = models.IntegerField
    unitssold = models.IntegerField
    operatingprofit = models.IntegerField
    operatingmargin = models.IntegerField
    