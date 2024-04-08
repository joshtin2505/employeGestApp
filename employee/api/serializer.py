from rest_framework import serializers
from employee.models import Empleado, Email, Telefono


class EmpleadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empleado
        fields = '__all__'

class EmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Email
        fields = '__all__'

class TelefonoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Telefono
        fields = '__all__'

