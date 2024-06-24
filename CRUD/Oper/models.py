
from django.db import models

class brillentsec(models.Model):
    SrNo = models.AutoField(primary_key=True,null=False)  
    SerialNumber = models.CharField(max_length=500,null=True)  
    CompName=models.CharField(max_length=500,null=True)
    ActivationCode = models.CharField(max_length=500,null=True) 
    ExpiryDate= models.CharField(max_length=500,null=True) 
    StartDate= models.CharField(max_length=500,null=True) 
    CheckedOn= models.CharField(max_length=500,null=True) 
    MacAddress= models.CharField(max_length=500,null=True) 
    Activated =models.CharField(max_length=500,null=True) 
    CheckedDt =models.CharField(max_length=500,null=True) 
    class Meta:
        db_table='brillentsec'

class feedcalcusers(models.Model):
    Id=models.AutoField(primary_key=True,null=False)
    username=models.CharField(max_length=500,null=True)
    password=models.CharField(max_length=500,null=True)
    confirm_password=models.CharField(max_length=500,null=True)
    class Meta:
        db_table='feedcalcusers'

