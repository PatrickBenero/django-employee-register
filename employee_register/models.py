from django.db import models

# Create your models here.

class position(models.Model):
    Title=models.CharField(max_length=50)

    def __str__(self):
        return self.Title

class Employee(models.Model):
    fullname=models.CharField(max_length=100)
    emp_code=models.CharField(max_length=3)
    mobile=models.CharField(max_length=15)
    position=models.ForeignKey(position,on_delete=models.CASCADE)

