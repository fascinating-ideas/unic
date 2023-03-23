from django.db import models

# Create your models here.
 
class user(models.Model):
    username=models.CharField(max_length=15)
    password=models.CharField(max_length=8)
    class Meta:  
        db_table = "employee" 
class book(models.Model):
    From=models.CharField(max_length=30)
    To=models.CharField(max_length=30)
    Date=models.CharField(max_length=15)
    returnDate=models.CharField(max_length=15)
    passengers=models.CharField(max_length=15)
    class Meta:  
        db_table = "book" 
class contact(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    phonenumber=models.CharField(max_length=10)
    message=models.CharField(max_length=300000)
    class Meta:  
        db_table = "contact" 
