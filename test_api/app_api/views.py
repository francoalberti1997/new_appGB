from django.shortcuts import render, HttpResponse

# Create your views here.

def productos(request):
    return HttpResponse("Esta es la API pero con texto")