from django.db import models
from enum import Enum
from .bankdetails import BankDetails
from .auth import User_Model

class InvoiceType(Enum):
    PROFORMA = "PF"
    PRESHIPMENT = "PS"
    COMMERCIAL = "CM"
    GST = "GS"
    PACKAGING = "PK"

class Member(models.Model):
    user = models.ForeignKey(User_Model,on_delete=models.CASCADE)
    companyname = models.CharField(max_length=100, null=False)
    address = models.CharField(max_length=200,null=False,default="n/a")
    gst = models.CharField(max_length=100,null=False,default="n/a")
    ref = models.CharField(max_length=100, null=False, unique=True)
    bankdetails = models.ForeignKey(BankDetails,on_delete=models.CASCADE )


class ChainInvoices(models.Model):
    name = models.CharField(max_length=200)
    description =  models.TextField()
    consigner = models.ForeignKey(Member,on_delete=models.CASCADE)
    consignee = models.CharField(max_length=200)
    ref = models.CharField(max_length=100)
    orderno = models.CharField(max_length=100, default=None, null=True)
    orderdate = models.DateTimeField(default=None,null=True)
    buyer = models.CharField(max_length=200)
    countryoforigin = models.CharField(max_length=100)
    countryofdestination = models.CharField(max_length=100)
    termsofdelivery = models.CharField(max_length=100)
    paymentterms = models.TextField()
    precarrigemode = models.CharField(max_length=100)
    vesselno = models.CharField(max_length=100, default=None, null=True)
    portofdischarge = models.CharField(max_length=100)
    placeofreceipt = models.CharField(max_length=100)
    placeofloading = models.CharField(max_length=100)
    finaldestination = models.CharField(max_length=100)
    invoiceitems = models.TextField()
    totalcartons =  models.IntegerField(default=0)
    netweight = models.IntegerField(default=0)
    grossweight = models.IntegerField(default=0)
    unit =  models.CharField(max_length=10)
    variationpercentage =  models.CharField(max_length=20)
    amountinwords =  models.CharField(max_length=255)
    amount =  models.IntegerField(default=0)
    amountunit = models.CharField(default="",max_length=255)
    exporterbankdetails = models.ForeignKey(BankDetails,on_delete=models.CASCADE)
    importerbankdetails = models.TextField(default=None, null=True)
    dutydrawback =  models.CharField(max_length=200,default=None, null=True)
    roadtep = models.CharField(max_length=200,default=None, null=True)
    igst =  models.CharField(max_length=200,default=None, null=True)
    isProFormaInvoiceCreated = models.BooleanField(default=False)
    isGstInvoiceCreated =  models.BooleanField(default=False)
    isPreShipmentCreted = models.BooleanField(default=False)
    isCommercialInvoiceCreated =  models.BooleanField(default=False)
    isPackegingInvoiceCreated =  models.BooleanField(default=False)
    datecreated = models.DateTimeField(auto_now_add=True)

