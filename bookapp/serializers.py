from rest_framework import serializers
from bookapp.models import HotelsAndRestraunts
from django.contrib.auth import authenticate

class HotelSerializer(serializers.ModelSerializer):
    class Meta: 
        model= HotelsAndRestraunts
        fields = '__all__'


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(username=data['username'], password=data['password'])
        if user is None:
            raise serializers.ValidationError('Invalid credentials')
        return data   