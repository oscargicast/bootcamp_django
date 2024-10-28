from django.contrib import admin
from django.urls import path

from django.http import HttpResponse

from products.views import all_products


def welcome_to_bootcamp(request):
    return HttpResponse("Bienvenidos al bootcamp!")


urlpatterns = [
    path('admin/', admin.site.urls),
    path('bienvenidos/', welcome_to_bootcamp),
    path('productos/', all_products),
]
