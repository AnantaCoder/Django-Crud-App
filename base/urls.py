from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Homepage
    # path('room/', views.room, name='room'),  # Add this line
    path('room/<str:pk>/', views.room, name='room'),  # Keep this if you need dynamic rooms
]
