from django.shortcuts import render
from django.conf import settings

from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from django.template import loader
from django.template import RequestContext

# from . utils import *
from . serializers import *
import json
from collections import OrderedDict

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from webllisto_backend.tasks import send_contact_email

# Create your views here.


class ContactusAPIView(APIView):
    serializer_class = ContactSerializer

    __doc__ = "Contact us API"

    def post(self,request):
        try:                         
            contact_serializer = ContactSerializer(data=request.data)                      
            if contact_serializer.is_valid():
                contact_serializer.save()                
                send_contact_email({'data':request.data})        
                             
                return Response({                    
                    'status': True,
                    'message' : 'Thankyou for contacting us'                    
                }, status=status.HTTP_200_OK)           
            else:
                message = contact_serializer.errors                
                return Response({'status': False,
                                 'message': message},
                                status=status.HTTP_400_BAD_REQUEST)
              
        except Exception as e:
            return Response({'status': False,
                             'message': str(e)},
                            status=status.HTTP_400_BAD_REQUEST)   


