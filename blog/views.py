from django.shortcuts import render
from django.http import HttpResponse
import random

def my_view(request):
    return HttpResponse(f"Привет, это текстовый ответ!Номером {random.randint(1,100)}")

def html_view(request):
    return render(request, "posts/index.html")