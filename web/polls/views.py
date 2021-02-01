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

from django.shortcuts import render
from django.http import HttpResponse
from cryptography import x509
from cryptography.hazmat.backends import default_backend
import subprocess

# Create your views here.


def index(request):
    host = request.META['HTTP_HOST']
    pem_data = (request.META["CLIENT_CERT"])
    print(pem_data)
    cert = x509.load_pem_x509_certificate(str.encode(pem_data), default_backend())
    var = cert.serial_number
    2
    print('Hello world host:       %s' % cert.issuer)
    print(type(cert))
    yuh = str(cert.issuer)

    yuh = yuh.strip('<')
    print(yuh)
    return HttpResponse("Hello world: %s " % yuh)
