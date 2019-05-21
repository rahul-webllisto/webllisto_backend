from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.

class Contact(models.Model):
	name = models.CharField(max_length=30)
	phone = PhoneNumberField()
	email = models.EmailField(max_length=30)
	detail = models.TextField()

	def __str__(self):
		return self.email