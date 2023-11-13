from django.urls import path
from . import views

urlpatterns = [
    path('create-room/', views.create_room, name='create_room'),
    path('update-room/<int:room_id>/', views.update_room, name='update_room'),
    path('delete-room/<int:room_id>/', views.delete_room, name='delete_room'),
    path('get-room/<int:room_id>/', views.get_room, name='get_room'),
    path('get-all-room/', views.get_all_room, name='get_all_room'),
]

