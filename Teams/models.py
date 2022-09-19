from django.db import models

# Create your models here.


class Team(models.Model):
    name = models.CharField(max_length=60, default = "Football Team" , null=False, blank = False)
    home = models.CharField(max_length=50, default = "Home" ,null = False , blank = False)


def __str__(self):
        return self.name
