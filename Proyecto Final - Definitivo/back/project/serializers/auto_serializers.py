from rest_framework import serializers
from api.models.auto import Auto

class AutoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Auto

        fields = ['id','marca','velocidad','placa','color']
