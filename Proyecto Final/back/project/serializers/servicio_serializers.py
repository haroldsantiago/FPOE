from rest_framework import serializers
from api.models.servicio import Servicio

class ServicioSerializers(serializers.ModelSerializer):
    class Meta:
        model = Servicio

        fields = ['id','nombre','cedula','descripcion','valor']