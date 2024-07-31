from django.db import models
from django.contrib.auth.models import AbstractUser

class District(models.Model):
    State = models.CharField(default='Sikkim')
    District=models.CharField(max_length=30)
    DistrictCode= models.CharField(max_length=90)
    def __str__(self):
        return self.State
    
class HotelsAndRestraunts(models.Model):
    HotelName= models.CharField(max_length=190)
    HotelOwner= models.CharField(max_length=70)
    phonenumber = models.CharField(max_length=10)
    Remarks = models.CharField(max_length= 900)   
# User Model

# class CustomUser(AbstractUser):
#     phonenumber = models.CharField(max_length=10, default='9999999999')
#     def __str__(self):
#         return self.username
