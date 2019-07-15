from rest_framework import serializers
from api.models import Card

class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = ('name', 'meaning', 'reversal', 'card_id', 'image')

