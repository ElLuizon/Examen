from django.db import models

# Create your models here.


class GStadium(models.Model):
    name = models.CharField(max_length=60, default="Football Stadium" , blank = False , null = False)
    location = models.CharField(max_length=100, blank = False, null=False)
    sponsor = models.CharField(max_length=25, blank = False, null = False)
    status = models.BooleanField(("Stadium disponibility"), default=True)

def __str__(self):
        return self.name