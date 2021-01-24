from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import render, get_object_or_404
from .models import Question
from subprocess import run, PIPE
import sys


# Create your views here.


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})


def external(request):
    inp = request.POST.get('param')
    out = run([sys.executable, 'C:\\Users\\toj90\\PycharmProjects\\untitled1\\web\\external_data.py', inp], shell=True, stdout=PIPE)
    print(out)
    return render(request, 'polls/detail.html', {'data1': out.stdout.decode('UTF-8')})
