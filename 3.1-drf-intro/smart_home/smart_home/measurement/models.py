from django.db import models

# TODO: опишите модели датчика (Sensor) и измерения (Measurement)

class Sensor(models.Model):
    name = models.CharField(max_length=50, verbose_name='название')
    description = models.CharField(max_length=150, verbose_name='описание')

    class Meta:
        verbose_name = 'Датчик'
        verbose_name_plural = 'Датчики'

    def __str__(self):
        return self.name
    
class Measurement(models.Model):
    
    temperature = models.DecimalField(max_digits=3, decimal_places=1, verbose_name='температура при измерении')
    date_measurement = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='measurements/', null=True, blank=True)
    sensor_id = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='measurements')

    class Meta:
        verbose_name = 'Измерение'
        verbose_name_plural = 'Измерения'

    def __str__(self):
        return f'Температура {self.temperature}°C в {self.sensor.name}'    
