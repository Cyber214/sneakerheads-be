from .models import Sneaker
from django.http import JsonResponse
from .serializers import SneakerSerializer
from rest_framework.decorators import api_view

@api_view(['GET'])
def allsneakers(request):
  all_sneakers = Sneaker.objects.all()
  serializer = SneakerSerializer(all_sneakers, many=True)
  return JsonResponse({'sneakers': serializer.data}, safe=False)