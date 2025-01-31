from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Homepage
    path('room/<str:pk>/', views.room, name='room'),  # Dynamic room page
    path('create_room/', views.createRoom, name='create-room'),  # Create room page
    path('update_room/<str:pk>/', views.updateRoom, name='update-room'),  # Update room page
    path('delete_room/<str:pk>/', views.deleteRoom, name='delete-room'),  # Delete room page
]