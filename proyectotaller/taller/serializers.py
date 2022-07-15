from .models import Atencion
from rest_framework import serializers

class AtencionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Atencion
        fields = '__all__'