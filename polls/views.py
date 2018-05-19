from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def index(request):
    return HttpResponse("Olá Mundo, Você está no mundo das enquetes.")

def detail(request, question_id):
    return HttpResponse("Você está vendo a pergunta %s" % question_id)

def results(request, question_id):
    response = "Você está vendo o resultado da pergunta %s"
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("Você está votando na questão %s" % question_id)
