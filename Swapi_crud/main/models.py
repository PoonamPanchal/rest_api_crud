from django.db import models

# Create your models here.
class People(models.Model):
    name=models.CharField(max_length=100 ,default='')
    height=models.CharField(max_length=500,default='')
    mass=models.CharField(max_length=100,default='')
    hair_color=models.CharField(max_length=100,default='')
    skin_color=models.CharField(max_length=100,default='')
    eye_color=models.CharField(max_length=100,default='')
    birth_year=models.CharField(max_length=100,default='')
    gender=models.CharField(max_length=100,default='')
    homeworld=models.CharField(max_length=500,default='')
    films=models.CharField(max_length=500,default='')
    species=models.CharField(max_length=500,default='')
    vehicles=models.CharField(max_length=500,default='')
    starships=models.CharField(max_length=500,default='')
    created=models.CharField(max_length=300,default='')
    edited=models.CharField(max_length=300,default='')
    url=models.CharField(max_length=200,default='')
    def __str___(self):
        return self.name
    
