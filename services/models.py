from django.db import models
from accounts.models import User

# Create your models here.


class Service(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return str(self.name)

class SubService(models.Model):
    service         = models.ForeignKey(Service, on_delete=models.CASCADE)
    name            = models.CharField(max_length=150)
    papers          = models.CharField(max_length=400 , blank=True , default="")
    actions         = models.CharField(max_length=400, blank=True , default="")

    def __str__(self):
        return self.name


class Order(models.Model):
    RECIVED         ="recived"
    PAID            ="paid"
    PROCESSING      ="processing"
    SENDTODELIVARY  ="sendToDelivary"
    CANCELED        ="canceled"
    FAILED          ="failed" 
    orderStatuses = (
        (RECIVED, "recived"),
        (PAID, "paid"),
        (PROCESSING, "processing"),
        (SENDTODELIVARY, "sendToDelivary"),
        (CANCELED, "canceled"),
        (FAILED, "failed"))



    CASH        = "cash on delivery"
    VISA        = "visa card"
    paymentTypes = (
        (CASH, "cash on delivery"),
        (VISA, "visa card"))
    user                = models.ForeignKey(User, on_delete=models.SET_NULL , null=True , blank=False)
    username            = models.CharField(max_length=20)
    service             = models.ForeignKey(Service, on_delete=models.SET_NULL , null=True , blank=False)
    serviceName         = models.CharField(max_length=150)
    subService          = models.ForeignKey(SubService, on_delete=models.SET_NULL , null=True , blank=False)
    subServiceName      = models.CharField(max_length=150)
    paymentType         = models.CharField(max_length=20, choices=paymentTypes, default=CASH)
    status              = models.CharField(max_length=20, choices=orderStatuses, default=RECIVED)
    

    def __str__(self):
        return self.username

class SubServiceParameter(models.Model):
    subService          = models.ForeignKey(SubService, on_delete=models.CASCADE , null=True , blank=False)
    subServiceName      = models.CharField(max_length=150)
    paramName           = models.CharField(max_length=150)
    isRequired          = models.BooleanField(default=True)
    paramType           = models.CharField(max_length=150)
    conditions          = models.CharField(max_length=300)


    def __str__(self):
        return self.username
