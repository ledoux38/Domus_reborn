from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render, get_object_or_404

from .forms import SensorForm
from .models import Sensor


# Create your views here.
def receive_sensor_data(request):
    return JsonResponse({'status': 'success'})


def add_sensor(request):
    if request.method == 'POST':
        form = SensorForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/sensors/')
        else:
            form = SensorForm()

            return render(request, 'add_sensor.html', {'form': form})


def edit_sensor(request, sensor_id):
    sensor = get_object_or_404(Sensor, pk=sensor_id)
    if request.method == 'POST':
        form = SensorForm(request.POST, instance=sensor)
        if form.is_valid():
            return HttpResponseRedirect('/sensors/')
        else:
            form = SensorForm(instance=sensor)
            return render(request, 'edit_sensor.html', {'form': form})


def delete_sensor(request, sensor_id):
    sensor = get_object_or_404(Sensor, pk=sensor_id)
    sensor.delete()
    return HttpResponseRedirect('/sensors/')
