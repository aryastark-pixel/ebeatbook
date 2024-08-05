from django.shortcuts import render
from rest_framework.views import APIView
from .models import HotelsAndRestraunts
from .serializers import HotelSerializer, LoginSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status
from django.contrib.auth import authenticate




class HotelsAndRestuarantsApi(APIView):
    def get(self, request, pk=None, format=None):
        id=pk
        if id is not None:
            datas=HotelsAndRestraunts.objects.get(id=id)
            serializer=HotelSerializer(datas)
            return Response(serializer.data)
        datas = HotelsAndRestraunts.objects.filter()
        serializer = HotelSerializer(datas, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class HotelsAndRestuarantsApiPost (APIView):   
    def post(self, request, format = None):
        serializer = HotelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']
            
            # Authenticate the user
            user = authenticate(request, username=username, password=password)
            if user is not None:
                # Generate JWT tokens
                refresh = RefreshToken.for_user(user)
                return Response({
                    'refresh': str(refresh),
                    'access': str(refresh.access_token),
                })
            else:
                return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Create your views here.
