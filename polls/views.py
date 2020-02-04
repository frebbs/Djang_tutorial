# Modules
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
# from django.template import loader
from .models import Question

# Create your views here.


def index(req):
    return render(req, 'polls/index.html', {
        'latest_question_list': Question.objects.order_by('-pub_date')[:5]
    })


def detail(req, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(req, 'polls/details.html', {'question': question})


def results(res, question_id):
    res = "You are seeing the results of question %s."
    return HttpResponse(res % question_id)


def vote(req, question_id):
    return HttpResponse('You are voting on question %s.' % question_id)

