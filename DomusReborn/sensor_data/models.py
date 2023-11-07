from django.db import models


# Create your models here.
class Sensor(models.Model):
    SENSOR_TYPES = (('TEMP', 'Temperature'),
                    ('HUM', 'Humidity'),
                    ('LIGHT', 'Light'))
    name = models.CharField(max_length=255, unique=True)
    sensor_type = models.CharField(max_length=5, choices=SENSOR_TYPES)
    location = models.CharField(max_length=255, null=True, blank=True)
    last_reading = models.FloatField(null=True, blank=True)
    last_reading_time = models.DateTimeField(null=True, blank=True)
    is_active = models.BooleanField(default=True)


def __str__(self):
    return self.name


def save(self, *args, **kwargs):
    super().save(*args, **kwargs)


class Meta:
    verbose_name = "Sensor"
    verbose_name_plural = "Sensors"
