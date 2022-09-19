from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from django.contrib import messages
from .models import Team
from .forms import TeamForm, UpdateForm
# Create your views here.



class CreateTeam(generic.CreateView):
    template_name="Teams/create_Team.html"
    model = Team
    form_class = TeamForm
    success_url = reverse_lazy("Teams:list_team")


class ListTeam(generic.View):
    template_name = "Teams/list_team.html"

    def get(self , request, *args , **kwargs):
        queryset = Team.objects.all()
        context = {
            "Teams": queryset
        }
        return render (request,self.template_name,context)


class UpdateTeam(generic.UpdateView):
    template_name = "Teams/update_team.html"
    model = Team
    form_class = UpdateForm
    success_url = reverse_lazy("Teams:list_team")

class DeleteTeam(generic.DeleteView):
    template_name = "Teams/delete_team.html"
    model = Team
    success_url = reverse_lazy("Teams:list_team")