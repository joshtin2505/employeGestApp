from rest_framework.routers import DefaultRouter
from employee.api.views import EmpleadoViewSet, EmailViewSet, TelefonoViewSet

router = DefaultRouter()
router.register('empleados', EmpleadoViewSet, basename='empleado')
router.register('emails', EmailViewSet, basename='email')
router.register('telefonos', TelefonoViewSet, basename='telefono')

urlpatterns = router.urls
