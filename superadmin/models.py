from django.db import models
from admin1.models import Staff

# Create your models here.
class Data(models.Model):
    username=models.TextField(max_length=20,db_column="username")
    password=models.TextField(max_length=20,db_column="password")
    
    class Meta:
        db_table="data"
        
