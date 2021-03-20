from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from .models import Question, Choice

# Create your views here.

class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "questions"
    def get_queryset(self):
        return Question.objects.all()

class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"

def meme(request):
    return HttpResponse("<img src='https://sun9-73.userapi.com/impg/xfCeRe1sNazEK_eo5Jl6dPA9LQBZH_Uh0-mEdQ/zV-Gv48r7mw.jpg?size=600x457&quality=96&proxy=1&sign=d00ac6affba31ae3975c11b6c982d758&type=album'>")

class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"

def vote(request, q_id):
    choices = request.POST.getlist("choice")
    question = Question.objects.get(pk=q_id) 
    for c_pk in choices:
        choice = question.choice_set.get(pk=c_pk)
        choice.votes += 1
        choice.save()
    return HttpResponseRedirect(reverse("polls:results", args=(q_id, )))