from rest_framework import serializers
from .models import Sensor, Measurement

# TODO: опишите необходимые сериализаторы

class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description']
    
    
class MeasurementSerializer(serializers.ModelSerializer):
    class Meta:
       model = Measurement
       fields = ['temperature', 'date_measurement', 'sensor_id', 'image']
    
    
class SensorDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = ['description']
        measurements = MeasurementSerializer(read_only=True, many=True)