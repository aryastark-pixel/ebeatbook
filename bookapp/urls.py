# all the urls here

from django.urls import path
from bookapp.views import HotelsAndRestuarantsApi, HotelsAndRestuarantsApiPost, LoginView
urlpatterns = [
    path('hotels/',HotelsAndRestuarantsApi.as_view(),name='gethotels'),
    path('hotels/post/',HotelsAndRestuarantsApiPost.as_view(),name='posthotels'),
     path('login/', LoginView.as_view(), name='login'),
     
]
