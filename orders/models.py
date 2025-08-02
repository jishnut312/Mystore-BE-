from django.db import models
from django.contrib.auth.models import User
# Create your models here.
# orders/models.py
class DeliveryAddress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    full_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    pincode = models.CharField(max_length=6)
    address = models.TextField()
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
