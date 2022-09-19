from django.db import models
from Teams.models import Team
# Create your models here.


CHOICES = (
    ("QB","Quarterback"),
    ("LO","Liniero Ofensivo"),
    ("C","Corredor"),
    ("CP","Corredor de poder"),
    ("TE","Tight End"),
    ("WR","Wide Receiver"),
    ("LB","Line Backer"),
    ("CB","Cornerback"),
    ("S","Safety"),
    ("K","Kicker"),
    ("P","Punter"),
    ("KR","Kick Returner"),
    ("PR","Punt Returner"),
    ("CL","Centro Largo"),
)

class Player(models.Model):
    name = models.CharField(max_length=50, blank=False , null = False )
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    position = models.CharField(max_length=32, default="Corredor", choices=CHOICES, blank = False, null = False)
    number = models.IntegerField(blank= False , null = False)
    status = models.BooleanField(("Player disponibility"), default=True)


def __str__(self):
        return self.name
