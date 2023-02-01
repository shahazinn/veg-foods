from django.db import models

# Create your models here.
class bitmartdb(models.Model):
    name=models.CharField(max_length=30, null=True, blank=True)
    image = models.ImageField(upload_to="profile", null=True, blank=True)
    email=models.CharField(max_length=30, null=True, blank=True)
    mob=models.IntegerField(null=True, blank=True)
    uname=models.CharField(max_length=30, null=True, blank=True)
    pswd=models.CharField(max_length=30, null=True, blank=True)
    cpswd=models.CharField(max_length=30, null=True, blank=True)
class bitdb(models.Model):
    name=models.CharField(max_length=30, null=True, blank=True)
    image = models.ImageField(upload_to="profile", null=True, blank=True)
    desc=models.CharField(max_length=30, null=True, blank=True)
class prodb(models.Model):
    category = models.CharField(max_length=30, null=True, blank=True)
    image = models.ImageField(upload_to="profile", null=True, blank=True)
    desc = models.CharField(max_length=30, null=True, blank=True)
    pname = models.CharField(max_length=30, null=True, blank=True)
    qua = models.IntegerField(null=True, blank=True)
    pri = models.IntegerField(null=True, blank=True)


