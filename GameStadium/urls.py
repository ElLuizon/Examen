from django.urls import path
from GameStadium import views

app_name = "gamestadium"

urlpatterns = [
    path('create_stadium/', views.CreateStadium.as_view(), name="create_stadium"),
    path('stadium_list/', views.StadiumList.as_view(),name="stadium_list"),
    path('update_stadium/<int:pk>/',views.UpdateStadium.as_view(),name="update_stadium"),
    path('delete_stadium/<int:pk>/',views.DeleteStadium.as_view(),name="delete_stadium"),
]