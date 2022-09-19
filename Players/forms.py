from dataclasses import fields
from django import forms

from .models import Player


class PlayerForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = "__all__"



class UpdatePlayerForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = "__all__"