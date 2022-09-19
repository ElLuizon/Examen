from django.urls import path
from Teams import views

app_name = "Teams"

urlpatterns=[
    path('create_team/', views.CreateTeam.as_view(), name="create_team"),
    path('list_team/', views.ListTeam.as_view(), name="list_team"),
    path('update_team/<int:pk>/', views.UpdateTeam.as_view(), name="update_team"),
    path('delete_team/<int:pk>/', views.DeleteTeam.as_view(), name="delete_team"),
]