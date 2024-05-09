from rest_framework.views import APIView
from rest_framework.response import Response
from ..serializers.auto_serializers import AutoSerializers
from api.models.auto import Auto
from rest_framework import status
from django.http import Http404


class Auto_APIView(APIView):
    def get(self, request, format=None, *args, **kwargs):
        auto = Auto.objects.all()
        serializer = AutoSerializers(auto, many=True)
        
        return Response(serializer.data)
    def post(self, request, format=None):
        serializer = AutoSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class Auto_APIView_Detail(APIView):
    def get_object(self, pk):
        try:
            return Auto.objects.get(pk=pk)
        except Auto.DoesNotExist:
            raise Http404
    def get(self, request, pk, format=None):
        auto = self.get_object(pk)
        serializer = AutoSerializers(auto)  
        return Response(serializer.data)
    def put(self, request, pk, format=None):
        auto = self.get_object(pk)
        serializer = AutoSerializers(auto, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk, format=None):
        auto = self.get_object(pk)
        auto.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)