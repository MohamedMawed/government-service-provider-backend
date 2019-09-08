from django.db import models
from accounts.models import User
import uuid
# Create your models here.


def upload_Geha_Image(instance, filename):
    return "geha/{filename}".format(filename=filename)


def upload_Office_Image(instance, filename):
    return "office/{filename}".format(filename=filename)


class Geha(models.Model):
    geha_id = models.AutoField(primary_key=True)
    geha_name = models.CharField(max_length=50)
    geha_icon = models.ImageField(upload_to=upload_Geha_Image)

    def __str__(self):
        return self.geha_name


class Office(models.Model):
    geha_id = models.ForeignKey(Geha, on_delete=models.CASCADE)
    off_id = models.AutoField(primary_key=True)
    off_name = models.CharField(max_length=150)
    off_icon = models.ImageField(
        upload_to=upload_Office_Image)

    def __str__(self):
        return self.off_name


class Service(models.Model):
    geha_id = models.ForeignKey(Geha, on_delete=models.CASCADE)
    off_id = models.ForeignKey(Office, on_delete=models.CASCADE)
    srv_id = models.AutoField(primary_key=True)
    srv_name = models.CharField(max_length=150)
    canBeOrdered = models.BooleanField(default=False)
    papers = models.TextField(blank=True, default="")
    actions = models.TextField(blank=True, default="")

    def __str__(self):
        return self.srv_name


class Order(models.Model):
    RECIVED = "recived"
    PAID = "paid"
    PROCESSING = "processing"
    SENDTODELIVARY = "send to delivary"
    DELIVARY = "delivered"
    CANCELED = "canceled"
    FAILED = "failed"
    orderStatuses = (
        (RECIVED, "recived"),
        (PAID, "paid"),
        (PROCESSING, "processing"),
        (SENDTODELIVARY, "sendToDelivary"),
        (DELIVARY, "delivered"),
        (CANCELED, "canceled"),
        (FAILED, "failed"))

    CASH = "cash on delivery"
    VISA = "visa card"
    paymentTypes = (
        (CASH, "cash on delivery"),
        (VISA, "visa card"))
    geha_id = models.ForeignKey(Geha, on_delete=models.CASCADE)
    ord_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=False)
    off_id = models.ForeignKey(
        Office, on_delete=models.SET_NULL, null=True, blank=False)
    srv_id = models.ForeignKey(
        Service, on_delete=models.SET_NULL, null=True, blank=False)
    ord_date = models.DateField(auto_now=True)
    ord_payment = models.CharField(
        max_length=20, choices=paymentTypes, default=CASH)
    status = models.CharField(
        max_length=20, choices=orderStatuses, default=RECIVED)

    def __str__(self):
        return str(self.user_id.full_name)


class ServiceParameter(models.Model):
    parm_id = models.AutoField(primary_key=True)
    srv_id = models.ForeignKey(
        Service, on_delete=models.CASCADE, null=True, blank=False)
    parm_name = models.CharField(max_length=50)
    is_rquired = models.BooleanField(default=True)
    parm_icon_name = models.CharField(max_length=50, blank=True)
    TEXT = "Text"
    NUMBER = "Number"
    DATE = "Date"
    CITY_LIST = "City List"
    paymentTypes = (
        (TEXT, "Text"),
        (NUMBER, "Number"),
        (DATE, "Date"),
        (CITY_LIST, "City List")
    )
    param_type = models.CharField(
        max_length=40, choices=paymentTypes, default=TEXT)
    conditions = models.TextField(blank=True)

    def __str__(self):
        return self.parm_name



class ServiceParameterAnswer(models.Model):
    ans_id = models.AutoField(primary_key=True)
    ord_id = models.ForeignKey(
        ServiceParameter, on_delete=models.CASCADE, null=True, blank=False)
    parm_id = models.ForeignKey(
        Service, on_delete=models.CASCADE, null=True, blank=False)
    parm_name = models.CharField(max_length=50)
    def __str__(self):
        return self.parm_name


class DelivaryPlaces(models.Model):
    place_id = models.AutoField(primary_key=True)
    geha_id = models.ForeignKey(
        Geha, on_delete=models.CASCADE, null=True, blank=False)
    place_name = models.CharField(max_length=100)
    def __str__(self):
        return self.place_name
