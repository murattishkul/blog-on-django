from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse
from .models import Question, Choice

def index(request):
    latest_response = Question.objects.order_by('-pub_date')[:5]
    output = ",".join(q.question_text for q in latest_response)
    return HttpResponse(output)

def suka(request):
    return HttpResponse('Everyone who reads this is suka!')

def detail(request, question_id):
    return HttpResponse('This is a detail view of a question: %s'  % Question.objects.get(pk=question_id) )

def results(request, question_id):
    suka = Choice.objects.all().filter( )
    return HttpResponse('These are the results of a question: %s' %  suka )

def vote(request, question_id):
    return HttpResponse('Vote on question: %s' % question_id)