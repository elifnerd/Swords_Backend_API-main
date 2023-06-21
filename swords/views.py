from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import SwordSerializer
from .models import Sword

@api_view(['GET', 'POST'])
def swords_list(request):
    if request.method == 'GET':
        swords = Sword.objects.all()
        serializer = SwordSerializer(swords, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = SwordSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)  

@api_view(['GET', 'PUT', 'DELETE'])
def swords_detail(request, pk):
    sword = get_object_or_404(Sword, pk=pk)
    if request.method == 'GET':
        serializer = SwordSerializer(sword);
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = SwordSerializer(sword, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == 'DELETE':
        sword.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    