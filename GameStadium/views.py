from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from django.contrib import messages
from .models import GStadium
from .forms import StadiumForm, UpdateStadiumForm

# Create your views here.


class CreateStadium(generic.CreateView):
    template_name = "stadiums/create_stadium.html"
    model = GStadium
    form_class = StadiumForm
    success_url = reverse_lazy("gamestadium:stadium_list")


class StadiumList(generic.View):
    template_name = "stadiums/stadium_list.html"
    def get (self, request, *args , **kwargs):
        queryset = GStadium.objects.filter(status=True)
        context = {
            "GameStadium":queryset
        }
        return render(request, self.template_name, context)


class UpdateStadium(generic.UpdateView):
    template_name = "stadiums/update_stadium.html"
    model = GStadium
    form_class = UpdateStadiumForm
    success_url = reverse_lazy("gamestadium:stadium_list")

class DeleteStadium(generic.DeleteView):
    template_name = "stadiums/delete_stadium.html"
    model = GStadium
    success_url = reverse_lazy("gamestadium:stadium_list")


