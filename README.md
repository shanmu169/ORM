# Ex01 Django ORM Web Application
## Date: 22-11-2025

## AIM
To develop a Django Application to store and retrieve data from a E-Commerce Website Database for Amazon or Flipkart using Object Relational Mapping(ORM).





## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Detect changes and create migration files that describe how to modify the database schema

### STEP 5:
Execute the migration files and update the database schema to match your Django models

### STEP 6:
Create a superuser with full access rights to all models and data through the admin interface.

### STEP 7:
Apply the migration files of the created app to the database

### STEP 8:
Execute Django admin using localhost and create details for 10 entries

## PROGRAM
```
models.py
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

admin.py
from django.contrib import admin
from.models import Categories,CategoriesAdmin
admin.site.register(Categories,CategoriesAdmin)
```


## OUTPUT
![alt text](<Screenshot 2025-11-22 084948.png>)


## RESULT
Thus the program for creating E-commerce website database using ORM hass been executed successfully
