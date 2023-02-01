from django.db import models

# Create your models here.
class CustomerDetailes(models.Model):
    username=models.CharField(max_length=100,null=True,blank=True)
    email=models.CharField(max_length=100,null=True,blank=True)
    password = models.CharField(max_length=100, null=True, blank=True)
    confirm_password= models.CharField(max_length=100, null=True, blank=True)

class adcontact(models.Model):
    name=models.CharField(max_length=100,null=True,blank=True)
    email=models.CharField(max_length=100,null=True,blank=True)
    message=models.CharField(max_length=100,null=True,blank=True)
