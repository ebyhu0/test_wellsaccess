from rest_framework import serializers
from wells.models import Psd


class PSD_Serializer(serializers.ModelSerializer):
    # profile = ProfileSerializer()

    class Meta:
        model = Psd
        fields = '__all__'
