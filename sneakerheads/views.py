from .models import Sneaker
from django.http import JsonResponse
from .serializers import SneakerSerializer
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404

@api_view(['GET'])
def sneakers(request):
  sneakers = Sneaker.objects.all()
  serializer = SneakerSerializer(sneakers, many=True)
  return JsonResponse({'sneakers': serializer.data}, safe=False)

@api_view(['POST'])
def newsneaker(request):
  serializer = SneakerSerializer(data=request.data)
  if serializer.is_valid():
    serializer.save()
    return JsonResponse({'message': 'Sneaker added successfully!', 'sneakers': serializer.data}, status=201)
  return JsonResponse(serializer.errors, status=400)

@api_view(['GET'])
def sneakerpage(request, sneakerId):
  sneaker = get_object_or_404(Sneaker, id=sneakerId)
  serializer = SneakerSerializer(sneaker)
  return JsonResponse(serializer.data, safe=False)