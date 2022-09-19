from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from django.contrib import messages
from .models import Player
from .forms import PlayerForm, UpdatePlayerForm

# Create your views here.


class CreatePlayer(generic.CreateView):
    template_name = "players/create_player.html"
    model = Player
    form_class = PlayerForm
    success_url = reverse_lazy("player:player_list")

class PlayerList(generic.View):
    template_name = "players/player_list.html"
    context = {}

    def get(self, request, *args, **kwargs):
        queryset = Player.objects.filter(status=True)
        self.context = {
            "Players": queryset
        }
        return render(request, self.template_name, self.context)

class UpdatePlayer(generic.UpdateView):
    template_name = "players/update_player.html"
    model = Player
    form_class = UpdatePlayerForm
    success_url = reverse_lazy("player:player_list")

class DeletePlayer(generic.DeleteView):
    template_name = "players/delete_player.html"
    model = Player
    success_url = reverse_lazy("player:player_list")