from django.urls import path
from . import views

urlpatterns = [
    path('ping/', views.ping_sensor, name='ping_sensor'),
    # path('receive-data/', views.ping_sensor, name='ping_sensor'),
    # path('ping/', views.receive_sensor_data, name='receive_sensor_data'),
    path('sensors-list/', views.sensors_list, name='sensors_list'),
    path('add-sensor/', views.add_sensor, name='add_sensor'),
    path('edit-sensor/<int:sensor_id>/', views.edit_sensor, name='edit_sensor'),
    path('delete-sensor/<int:sensor_id>/', views.delete_sensor, name='delete_sensor'),
]
