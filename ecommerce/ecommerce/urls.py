from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.http import HttpResponse
from django.urls import path, include

from rest_framework import routers

from apps.products.views import all_products
from apps.products.controllers import ThicknessViewSet


router = routers.DefaultRouter()

router.register(r'thickness', ThicknessViewSet)


def welcome_to_bootcamp(request):
    return HttpResponse('Bienvenidos al bootcamp!')


urlpatterns = [
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    path('api/products/', include('apps.products.urls')),
    path('admin/', admin.site.urls),
    path('bienvenidos/', welcome_to_bootcamp),
    path('productos/', all_products),
]


if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT,
    )
