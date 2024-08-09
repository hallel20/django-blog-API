from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView

# Create your views here.

def home(request):
    return HttpResponse("Hello World")