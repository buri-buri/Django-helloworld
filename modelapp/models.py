from django.db import models

class Student(models.Model):
    GENDERS=(
        ('f','Female'),
        ('m','Male'),
        ('u','Undisclosed')
    )
    name=models.CharField(max_length=100)
    roll_no=models.IntegerField(unique=True)
    address=models.TextField(null=True,blank=True)
    #charfield has limited caharcters but textfield not
    phone_number=models.CharField(max_length=15,null=True,blank=True)
    email=models.EmailField(null=True,blank=True)
    #e-mail field is just a varchar field with limit 255 chars
    gender=models.CharField(max_length=1,choices=GENDERS,null=True,blank=True)

    def __str__(self):
        return self.name