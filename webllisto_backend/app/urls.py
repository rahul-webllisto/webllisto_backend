from django.urls import path
from . views import *

urlpatterns = [
	path('contactus', ContactusAPIView.as_view(), name="contact_us"),
]
    
