from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello World. You are at the polls page")

def detail(request,question_id):
    return HttpResponse("You're looking at question {}".format(question_id))

def results(request, question_id):
    response = "You're looking at results of question {}"
    return HttpResponse(response.format(question_id))

def vote(request, question_id):
    return HttpResponse("You're voting on question {}".format(question_id))

