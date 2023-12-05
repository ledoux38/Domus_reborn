import json

import requests
from django.http import HttpResponseRedirect
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404

from .forms import SensorForm, SensorGroupForm
from .models import Sensor


# Create your views here.
def receive_sensor_data(request):
    return JsonResponse({'status': 'success'})


def add_sensor(request):
    form = SensorGroupForm(request.POST or None)
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


def ping_sensor(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)  # Parse les données JSON du corps de la requête
            sensor_ip = data.get('sensorIp')
            sensor_port = data.get('sensorPort')

            # Votre logique de ping
            response = requests.get(f"http://{sensor_ip}:{sensor_port}/ping")
            if response.status_code == 200:
                return JsonResponse({'success': True})
            else:
                return JsonResponse({'success': False})
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
        except requests.ConnectionError:
            return JsonResponse({'success': False})


def sensors_list(request):
    sensors = Sensor.objects.all()  # Récupère tous les objets Sensor de la base de données
    return render(request, 'sensor_data/sensors_list.html', {'sensors': sensors})
