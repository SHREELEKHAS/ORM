from django.db import models
from django.contrib import admin
class book(models.Model):
 name=models.CharField(max_length=20);
 author=models.CharField(max_length=20);
 publisher=models.CharField(max_length=20);
 publish_year=models.IntegerField();
 code=models.CharField(max_length=20,primary_key=True);
 price=models.IntegerField();
class bookAdmin(admin.ModelAdmin):
 list_display=("name","author","publisher","publish_year","code","price");
