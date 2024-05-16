from rest_framework.response import Response
from rest_framework.views import APIView
from ..serializers.computador_serializer import ComputadorSerializers
from api.models.computador import Computador
from rest_framework import status
from django.http import Http404


class Computador_APIView(APIView):
    def get(self, request, format=None, *args, **kwargs):
        computador = Computador.objects.all()
        serializer = ComputadorSerializers(computador, many=True)
        
        return Response(serializer.data)
    def post(self, request, format=None):
        serializer = ComputadorSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class Computador_APIView_Detail(APIView):
    def get_object(self, pk):
        try:
            return Computador.objects.get(pk=pk)
        except Computador.DoesNotExist:
            raise Http404
    def get(self, request, pk, format=None):
        computador = self.get_object(pk)
        serializer = ComputadorSerializers(computador)  
        return Response(serializer.data)
    def put(self, request, pk, format=None):
        computador = self.get_object(pk)
        serializer = ComputadorSerializers(computador, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk, format=None):
        computador = self.get_object(pk)
        computador.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
