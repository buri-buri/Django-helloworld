from django.db import models
from modelapp.validators import validate_even_number
from django.core.validators import (
    EmailValidator,
    MaxValueValidator,
    MinValueValidator,
    URLValidator,
    validate_slug,
)
class Student(models.Model):
    GENDERS=(
        ('f','Female'),
        ('m','Male'),
        ('u','Undisclosed')
    )
    name=models.CharField(max_length=100)
    roll_no=models.IntegerField(unique=True)
    address=models.TextField(null=True,blank=True)
    phone_number=models.CharField(max_length=15,null=True,blank=True)
    email=models.CharField(max_length=100,null=True,blank=True,
    validators=[EmailValidator("Invalid Email")])
    gender=models.CharField(max_length=1,choices=GENDERS,null=True,blank=True)
    age=models.IntegerField(null=True,blank=True,
    validators=[
        MaxValueValidator(125),
        MinValueValidator(2),
        validate_even_number
    ])
    slug=models.CharField(max_length=100,validators=[validate_slug],null=True,blank=True)
    def __str__(self):
        return self.name