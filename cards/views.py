from django.shortcuts import render
from .models import Card

def cards(request):
    card = Card.objects.all().order_by("box","-date_create")
    context = {
        'card' : card
    }
    return render(request,"index_cards.html", context)
