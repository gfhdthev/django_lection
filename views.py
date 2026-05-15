from django.shortcuts import render

# core/views.py
from django.http import HttpResponse

def hello_world(request):
    return HttpResponse("<h1>Привет, это моя первая страница!</h1>")