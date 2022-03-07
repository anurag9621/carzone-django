from django.shortcuts import render
from . import views

# Create your views here.
def cars(request):
    return render(request, 'cars/cars.html')