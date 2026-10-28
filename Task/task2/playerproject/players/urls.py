from django.urls import path
from . import views

urlpatterns = [
    path('players/', views.create_player),
    path('players/all/', views.get_players),
    path('players/update/<int:id>/', views.update_player),
    path('players/delete/<int:id>/', views.delete_player),
]