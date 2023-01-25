from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Question

# Create your views here.
def index(request):
    # return HttpResponse("Hello, welcome to the polls index.")
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    # output = ', '.join([q.question_text for q in latest_question_list])
    template = loader.get_template('polls/index.html')
    context = {'latest_question_list': latest_question_list}
    return HttpResponse(template.render(context,request))

def detail(request, question_id):
    return HttpResponse("You are viewing question %s." %question_id)

def results(request, question_id):
    return HttpResponse("You are viewing the results of question %s." %question_id)

def vote(request, questions_id):
    return HttpResponse("You are voting on question %s." %questions_id)