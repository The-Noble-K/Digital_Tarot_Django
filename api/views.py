from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from api.models import Card

@api_view(["GET"])
def card(request):
    cards = Card.objects.all()
    return Response(status=status.HTTP_200_OK, data={"data": cards})


