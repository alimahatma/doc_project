from django.shortcuts import render
from home.models import Artikel


def index_home(request):
    return render(request, 'index_home.html')

def research(request):
    researchs = Artikel.objects.all()
    context = {
        'researchs' : researchs
    }
    
    return render(request, 'research.html', context)

