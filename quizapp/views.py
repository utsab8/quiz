from django.shortcuts import render
from quizapp.models import Quiz
# Create your views here.

def qpage(request):
    question = Quiz.objects.all()
    
    return render(request, 'quiz.html', {'question': question})