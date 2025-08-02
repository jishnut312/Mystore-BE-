from rest_framework import serializers
from orders.models import DeliveryAddress

class DeliveryAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeliveryAddress
        fields = ['full_name', 'phone', 'pincode', 'address', 'city', 'state']
