from django import forms
from .models import Team


class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = "__all__"



class UpdateForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = "__all__"