from django.db import models

# Create your models here.


class Contact(models.Model):
    Sno = models.AutoField
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    number = models.CharField(max_length=12)
    cservices = models.CharField(max_length=100)
    textarea = models.CharField(max_length=1000)


    def __str__(self):
        return self.name