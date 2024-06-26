from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'illustrations/index.html')

def artists(request):
    return render(request, 'illustrations/artists.html')

def contact(request):
    return render(request, 'illustrations/contact.html')