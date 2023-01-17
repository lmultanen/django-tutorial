from django.shortcuts import render
import datetime
from django.http import HttpResponse

# Create your views here.
def my_app(request):
    time = datetime.datetime.now()
    response = "<h1> The current time is " + str(time) + "</h1>"
    return HttpResponse(response)