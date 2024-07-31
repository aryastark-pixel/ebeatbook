# all the urls here

from django.urls import path
from bookapp.views import HotelsAndRestuarantsApi, HotelsAndRestuarantsApiPost
urlpatterns = [
    path('hotels/',HotelsAndRestuarantsApi.as_view(),name='gethotels'),
    path('hotels/post/',HotelsAndRestuarantsApiPost.as_view(),name='posthotels'),
]
