from rest_framework.decorators import api_view
from rest_framework.response import Response
from.serializers import SwordSerializer
from .models import Sword

@api_view(['GET'])
def swords_list(request):
    swords = Sword.objects.all()
    
    serializer = SwordSerializer(swords, many=True)
    
    return Response(serializer.data)