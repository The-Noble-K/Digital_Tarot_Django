from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from api.models import Card
from api.serializers import CardSerializer

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

@api_view(["GET"])
def card(request):
    cards = Card.objects.all()
    serializer = CardSerializer(cards, many=True)
    return JsonResponse(serializer.data, status=status.HTTP_200_OK, safe=False)


