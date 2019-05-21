from rest_framework import serializers
from . models import *



class ContactSerializer(serializers.ModelSerializer):
    def validate(self, data, *args, **kwargs):
        return super(ContactSerializer, self).validate(data, *args, **kwargs)

    def create(self, validated_data):        
        name=validated_data['name']
        phone = validated_data['phone']
        email = validated_data['email']
        detail = validated_data['detail']
        contact = Contact.objects.create(**validated_data)
        contact.save()
        return contact


    class Meta:
        model = Contact
        fields = ('name', 'phone', 'email',
                  'detail',)
