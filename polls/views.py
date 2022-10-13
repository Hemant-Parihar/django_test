from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'home.html', {'name': 'Hemant'})

def result(request):
    # firstNumber = request
    firstNumber = int(request.POST["first number"])
    secondNumber = int(request.POST["seond number"])
    ans = firstNumber + secondNumber
    return render(request, 'result.html', {'ans': ans})