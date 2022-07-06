from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('Hi!')


def detail(request, question_id):
    return HttpResponse(f'You are looking at question - {question_id}')


def results(request, question_id):
    response = f"You're looking at the results of question {question_id}."
    return HttpResponse(response, question_id)


def vote(request, question_id):
    return HttpResponse(f"You're voting on question {question_id}")
