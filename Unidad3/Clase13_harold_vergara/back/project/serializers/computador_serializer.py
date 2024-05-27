from rest_framework import serializers
from api.models.computador import Computador

class ComputadorSerializers(serializers.ModelSerializer):
    class Meta:
        model = Computador 
        fields = ["id", "marca", "procesador", "memoriaRam", "almacenamiento"]
