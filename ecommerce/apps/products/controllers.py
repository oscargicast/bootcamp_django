from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import viewsets
from rest_framework import mixins
from rest_framework import serializers
# from rest_framework import authentication, permissions

from apps.products.models import Material, Thickness


class ListMaterial(APIView):
    # authentication_classes = [authentication.TokenAuthentication]
    # permission_classes = [permissions.IsAdminUser]

    def get(self, request, format=None):
        materials = Material.objects.values(
            'id',
            'name',
        )
        return Response(materials)


class ThicknessSerializer(serializers.ModelSerializer):
    class Meta:
        model = Thickness
        fields = (
            'id',
            'material',
            'value_mm',
            'value_inch',
        )


# class ListThickness(
#     generics.GenericAPIView,
#     mixins.ListModelMixin,
#     mixins.RetrieveModelMixin,
# ):
#     queryset = Thickness.objects.all()
#     serializer_class = ThicknessSerializer
#     # permission_classes = [IsAdminUser]

#     def get(self, request, *args, **kwargs):
#         if 'pk' in kwargs:
#             return self.retrieve(request, *args, **kwargs)
#         return self.list(request, *args, **kwargs)


class ListThickness(generics.ListAPIView):
    queryset = Thickness.objects.all()
    serializer_class = ThicknessSerializer


class RetrieveThickness(generics.RetrieveAPIView):
    queryset = Thickness.objects.all()
    serializer_class = ThicknessSerializer


class ThicknessViewSet(viewsets.ModelViewSet):
    queryset = Thickness.objects.all()
    serializer_class = ThicknessSerializer
    # permission_classes = [IsAccountAdminOrReadOnly]

    def get_queryset(self):
        queryset = self.queryset
        query_params = self.request.query_params
        material_id = query_params.get('material_id')
        if material_id:
            queryset = queryset.filter(material_id=material_id)
        return queryset
