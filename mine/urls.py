from django.urls import path
from . import views

app_name = 'mine'

urlpatterns = [
    path('', views.index, name='index'),
    path('game/<str:difficulty>/', views.game, name='game'),
    path('save-time/', views.save_time, name='save_time'),
]