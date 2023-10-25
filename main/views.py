from django.shortcuts import render

from .models.models import *
# Create your views here.
def main_index(request):

    info = HomePage.objects.first()
    
    context = {
        'info': info, 
    }
    # Render the response and send it back!
    return render(request, 'home.html', context )