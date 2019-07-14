from django.contrib import admin
from api.models import Card

class CardAdmin(admin.ModelAdmin):
    pass

admin.site.register(Card, CardAdmin)

