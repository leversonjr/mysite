from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from .models import Question, Choice

def index(request):

    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {'latest_question_list': latest_question_list,}
    return HttpResponse(template.render(context, request))

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question':question})

def vote(request, question_id):
   question = get_object_or_404(Question, pk=question_id)
   try:
       selected_chocie = question.choice_set.get(pk=request.POST['choice'])
   except (KeyError, Choice.DoesNotExist):
       # volta a exibir o formulario de votação
        return render(request, 'polls/detail.html',{
            'question':question,
            'error_message': "Você não selecionou um opção"
        })
   else:
       selected_chocie.votes += 1
       selected_chocie.save()
       # Sempre retorna um HttpResponseRedirect após lidar com sucesso
       # com dados POST.Isso impede que os dados sejam postados duas vezes se
       # Usuário acessa o botão Voltar.

       return HttpResponseRedirect(reverse('polls:results', args=(question.id)))