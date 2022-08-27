"""itbank URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers

from clientes.views import UserViewSet
from prestamos.views import PrestamoViewSet
from sucursales.views import SucursalViewSet
from tarjetas.views import TarjetaViewSet

router = routers.DefaultRouter()
router.register(r'customers', UserViewSet, basename='customer')
router.register(r'loans', PrestamoViewSet, basename='loan')
router.register(r'cards', TarjetaViewSet, basename='card')
router.register(r'branches', SucursalViewSet, basename='branch')

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
