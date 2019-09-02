from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings



class User(AbstractUser):
    full_name = models.CharField(max_length=150)
    email = models.EmailField(null=False)
    avatar = models.CharField(max_length=200, blank=True,
                              default='/media/avatars/user/user.jpg')  # need to be tested and if you wanna rename, no prob
    password_unhashed = models.CharField(max_length=100, blank=True,)
    active = models.BooleanField("Is active ?",default=True)
    address = models.CharField(max_length=200, blank=False)
    government = models.CharField(max_length=100, blank=False)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'Customers'
        verbose_name_plural = 'Users'
