from xmlrpc.client import boolean
from django.shortcuts import render
from .models import Destination

# Create your views here.
def index(request):

    dest1 = Destination(1, "Chennai", "destination_1.jpg", "South City of India", 400, False)
    dest2 = Destination(2, "Kolkata", "destination_2.jpg", "City of briges.", 800, False)
    dest3 = Destination(3, "Gujrat", "destination_3.jpg", "Salt city.", 1000, True)

    dests = [dest1, dest2, dest3]

    return render(request, 'index copy.html', {'dests': dests})