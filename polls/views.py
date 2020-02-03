# Modules
from django.http import Http404
from django.shortcuts import render
from django.http import HttpResponse
# from django.template import loader
from .models import Question

# Create your views here.


def index(req):
    return render(req, 'polls/index.html', {
        'latest_question_list': Question.objects.order_by('-pub_date')[:5]
    })


def detail(req, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404('Im really sorry, I tried looking for that question, but it simply does not exist!')
    return render(req, 'polls/details.html', {
        'question': question
    })


def results(res, question_id):
    res = "You are seeing the results of question %s."
    return HttpResponse(res % question_id)


def vote(req, question_id):
    return HttpResponse('You are voting on question %s.' % question_id)

