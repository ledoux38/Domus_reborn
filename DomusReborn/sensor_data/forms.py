from django import forms

from .models import Sensor, SensorGroup


class SensorGroupForm(forms.ModelForm):
    class Meta:
        model = SensorGroup
        fields = ['name', 'location', 'ip_address', 'port', 'registration_key']
        widgets = {
            'ip_address': forms.TextInput(attrs={'id': 'sensorGroupIp', 'class': 'your-css-class'}),
            'port': forms.NumberInput(attrs={'id': 'sensorGroupPort', 'class': 'your-css-class'}),
            'registration_key': forms.TextInput(attrs={'id': 'sensorGroupKey', 'class': 'your-css-class'}),
            'name': forms.TextInput(attrs={'id': 'sensorGroupName', 'class': 'your-css-class'})
        }
        # Autres configurations de widget si nécessaire


# class SensorForm(forms.ModelForm):
#    class Meta:
#        model = Sensor
#        fields = ['id', 'group', 'sensor_type', 'last_reading', 'last_reading_time', 'is_active']
#        widgets = {
#            'sensor_type': forms.Select(attrs={'class': 'select-neon'}),
#            'ip_address': forms.TextInput(attrs={'id': 'sensorIp', 'class': 'your-css-class'}),
#            'port': forms.NumberInput(attrs={'id': 'sensorPort', 'class': 'your-css-class'}),
#            'registration_key': forms.TextInput(attrs={'id': 'sensorKey', 'class': 'your-css-class'})
#        }


class SensorForm(forms.ModelForm):
    class Meta:
        model = Sensor
        fields = ['id', 'sensor_type', 'last_reading', 'last_reading_time', 'is_active']
        widgets = {
            'id': forms.TextInput(attrs={'readonly': 'readonly'}),
            'sensor_type': forms.Select(attrs={'disabled': True}),
            'last_reading': forms.NumberInput(attrs={'readonly': 'readonly'}),
            'last_reading_time': forms.DateTimeInput(attrs={'readonly': 'readonly'}),
            'is_active': forms.CheckboxInput(attrs={'disabled': True}),
        }
