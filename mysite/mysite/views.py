from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    # return HttpResponse("Welcome to my first django site")
    return render(request, 'mysite/index.html')
    