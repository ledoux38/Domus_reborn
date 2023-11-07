from django.urls import path
from . import views

urlpatterns = [
    path('receive-data/', views.receive_sensor_data, name='receive_sensor_data'),
    path('add-sensor/', views.add_sensor, name='add_sensor'),
    path('edit-sensor/<int:sensor_id>/', views.edit_sensor, name='edit_sensor'),
    path('delete-sensor/<int:sensor_id>/', views.delete_sensor, name='delete_sensor'),
]
