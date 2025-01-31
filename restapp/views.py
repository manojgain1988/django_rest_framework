from django.shortcuts import get_object_or_404
from restapp.serializers import contactSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from restapp.models import contact
from rest_framework import status

# Create your views here.

class contactViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = contact.objects.all()
        serializer = contactSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = contact.objects.all()
        contact = get_object_or_404(queryset, pk=pk)
        serializer = contactSerializer(contact)
        return Response(serializer.data)
    

    def create(self,request):
        serializer = contactSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,  status=status.HTTP_201_CREATED)
        
    # def update(self, request, pk=None):
    #     Cont = contact.objects.get(pk=pk)
    #     serializer = contactSerializer(Cont, data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
