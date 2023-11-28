from django import forms

from .models import Sensor


class SensorForm(forms.ModelForm):
    class Meta:
        model = Sensor
        fields = ['name', 'sensor_type', 'location', 'last_reading', 'last_reading_time', 'is_active', 'ip_address',
                  'port', 'registration_key']
        widgets = {
            'sensor_type': forms.Select(attrs={'class': 'select-neon'}),
            'ip_address': forms.TextInput(attrs={'id': 'sensorIp', 'class': 'your-css-class'}),
            'port': forms.NumberInput(attrs={'id': 'sensorPort', 'class': 'your-css-class'}),
            'registration_key': forms.TextInput(attrs={'id': 'sensorKey', 'class': 'your-css-class'})
        }
