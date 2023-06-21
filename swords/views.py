from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from.serializers import SwordSerializer
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

@api_view(['GET'])
def swords_detail(request, pk):
    try:
        sword = Sword.objects.get(pk=pk)
        serializer = SwordSerializer(sword);
        return Response(serializer.data)
    except Sword.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    return Response(pk)
