from django.forms import forms

from DomusReborn.sensor_data.models import Sensor


class SensorForm(forms.ModelForm):
    class Meta:
        model = Sensor
        fields = ['name', 'sensor_type', 'localtion', 'is_active']
