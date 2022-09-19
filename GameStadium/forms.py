from django import forms

from .models import GStadium


class StadiumForm(forms.ModelForm):
    class Meta:
        model = GStadium
        fields = "__all__"



class UpdateStadiumForm(forms.ModelForm):
    class Meta:
        model = GStadium
        fields = "__all__"