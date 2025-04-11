from django.db import models

class BankDetails(models.Model):
    bankname = models.CharField(max_length=200)
    accountno = models.CharField(max_length=200,unique=True)
    ifsccode = models.CharField(max_length=200)
    branchname =  models.CharField(max_length=200)