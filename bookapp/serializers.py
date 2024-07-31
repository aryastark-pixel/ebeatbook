from rest_framework import serializers
from bookapp.models import HotelsAndRestraunts

class HotelSerializer(serializers.ModelSerializer):
    class Meta: 
        model= HotelsAndRestraunts
        fields = '__all__'
