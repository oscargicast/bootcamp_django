from django.urls import path
from apps.products.controllers import ListMaterial, ListThickness, RetrieveThickness

urlpatterns = [
    path('materials/', ListMaterial.as_view(), name='materials-list'),
    path('thicknesses/', ListThickness.as_view(), name='thicknesses-list'),
    path('thicknesses/<uuid:pk>/', RetrieveThickness.as_view(), name='thicknesses-detail'),
]
