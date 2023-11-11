from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render, get_object_or_404

from .forms import SensorForm
from .models import Sensor


# Create your views here.
def receive_sensor_data(request):
    return JsonResponse({'status': 'success'})


def add_sensor(request):
    form = SensorForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/sensors/')
    return render(request, 'sensor_data/manage_sensor.html', {'form': form, 'action': 'Add'})


def edit_sensor(request, sensor_id):
    sensor = get_object_or_404(Sensor, pk=sensor_id)
    form = SensorForm(request.POST or None, instance=sensor)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/sensors/')
    return render(request, 'sensor_data/manage_sensor.html', {'form': form, 'action': 'Edit', 'sensor': sensor})


def delete_sensor(request, sensor_id):
    sensor = get_object_or_404(Sensor, pk=sensor_id)
    sensor.delete()
    return HttpResponseRedirect('/sensors/')


def sensors_list(request):
    sensors = Sensor.objects.all()  # Récupère tous les objets Sensor de la base de données
    return render(request, 'sensor_data/sensors_list.html', {'sensors': sensors})
