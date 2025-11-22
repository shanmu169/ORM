from django.db import models
from django.contrib import admin

class Categories(models.Model):
    Serialno=models.AutoField(primary_key=True)
    Product_Name=models.CharField (max_length = 50)
    Price=models.FloatField()
    Date=models.DateField()
    Style=models.CharField(max_length=10)
    Time=models.TimeField()
    Product_details=models.TextField()
    Quantity=models.IntegerField()
    Expiry_date=models.DateField()
class CategoriesAdmin(admin.ModelAdmin):
    list_display=["Serialno","Product_Name","Price","Date","Time","Product_details","Quantity","Expiry_date"]



