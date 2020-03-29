from wells.models import Psd
from rest_framework import viewsets, permissions
from .serializers import PSD_Serializer

# PSD ViewSets


class PSDViewSet(viewsets.ModelViewSet):
    queryset = Psd.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = PSD_Serializer
