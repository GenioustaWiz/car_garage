from django.shortcuts import render

# Create your views here.
def main_index(request):


    # Render the response and send it back!
    return render(request, 'home.html', )