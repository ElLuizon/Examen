from django.urls import path
from Players import views


app_name ="player"

urlpatterns = [
    path('create_player/', views.CreatePlayer.as_view(), name="create_player"),
    path('player_list/', views.PlayerList.as_view(),name="player_list"),
    path('update_player/<int:pk>/', views.UpdatePlayer.as_view(),name="update_player"),
    path('delete_player/<int:pk>/', views.DeletePlayer.as_view(),name="delete_player"),
]