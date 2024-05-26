from rest_framework import serializers
from api.models.computador import Computador

class ComputadorSerializers(serializers.ModelSerializer):
    class Meta:
        model = Computador 
        exclude = ["id"]
