from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse

from django.views import generic
from .models import Question, Choice


class IndexView(generic.ListView):

   template_name = 'polls/index.html'
   context_object_name = 'latest_question_list'

   def get_queryset(self):
       ''' Retorna as ultimas 5 perguntas publicadas '''
       return Question.objects.order_by('-pub_date')[:5]

class DetailView(generic.DetailView):

    model = Question
    template_name = 'polls/detail.html'

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

def vote(request, question_id):
   question = get_object_or_404(Question, pk=question_id)
   try:
       selected_choice = question.choice_set.get(pk=request.POST['choice'])
   except (KeyError, Choice.DoesNotExist):
       # volta a exibir o formulario de votação
        return render(request, 'polls/detail.html',{
            'question': question,
            'error_message': "Você não selecionou um opção",
        })
   else:
       selected_choice.votes += 1
       selected_choice.save()
       # Sempre retorna um HttpResponseRedirect após lidar com sucesso
       # com dados POST.Isso impede que os dados sejam postados duas vezes se
       # Usuário acessa o botão Voltar.

       return HttpResponseRedirect(reverse(request, 'polls:results', args=(question.id,)))