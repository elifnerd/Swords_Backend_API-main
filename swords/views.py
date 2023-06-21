from rest_framework.decorators import api_view
from rest_framework.response import Response
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
        if serializer.is_valid() == True:
          serializer.save()
          return Response(serializer.data, status=201)  
        else:
            return Response(serializer.errors, status=400)
        