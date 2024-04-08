from rest_framework import viewsets
from employee.models import Empleado, Email, Telefono
from employee.api.serializer import EmpleadoSerializer, EmailSerializer, TelefonoSerializer

class EmpleadoViewSet(viewsets.ModelViewSet):
    queryset = Empleado.objects.all()
    serializer_class = EmpleadoSerializer

class EmailViewSet(viewsets.ModelViewSet):
    queryset = Email.objects.all()
    serializer_class = EmailSerializer

class TelefonoViewSet(viewsets.ModelViewSet):
    queryset = Telefono.objects.all()
    serializer_class = TelefonoSerializer