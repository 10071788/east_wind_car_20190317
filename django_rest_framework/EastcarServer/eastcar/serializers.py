from rest_framework import serializers
from .models import RentalCarInfo

class RentalCarSerializer(serializers.ModelSerializer):
    class Meta:
        model = RentalCarInfo
        fields = ('carid', 'srcaddr', 'dstaddr')