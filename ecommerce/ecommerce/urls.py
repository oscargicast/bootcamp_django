from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from django.http import HttpResponse

from apps.products.views import all_products


def welcome_to_bootcamp(request):
    return HttpResponse('Bienvenidos al bootcamp!')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('bienvenidos/', welcome_to_bootcamp),
    path('productos/', all_products),
]


if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT,
    )
