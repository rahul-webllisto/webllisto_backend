from rest_framework import serializers
from . models import *



class ContactSerializer(serializers.ModelSerializer):
    token = serializers.CharField()

    def validate(self, attrs):        
        token = attrs.get('token')
        if token == 'webllisto':           
            return attrs
        else:
            raise serializers.ValidationError("Invalid token!")

    def create(self, validated_data): 
        del validated_data['token']
        return Contact.objects.create(**validated_data)


    class Meta:
        model = Contact
        fields = ('token', 'name', 'phone', 'email',
                  'detail',)
