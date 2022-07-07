from django.shortcuts import render
from django.http import HttpResponse, Http404

from .models import Question


# Create your views here.
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:3]

    context = {
        'latest_question_list': latest_question_list
    }
    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    question = Question.objects.get(pk=question_id)

    context = {
        'question': question
    }

    return render(request, 'polls/detail.html', context)
'''
def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404('Question does not exist!')

    context = {
        'question': question
    }
    return render(request, 'polls/detail.html', context)
'''



def results(request, question_id):
    response = f"You're looking at the results of question {question_id}."
    return HttpResponse(response, question_id)


def vote(request, question_id):
    return HttpResponse(f"You're voting on question {question_id}")
