from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Question
from .models import Answer
from .forms import QuestionForm
from .forms import AnswerForm
from django.db.models import Q
from users.models import User

# Create your views here.

def home(request):
    """
    Allows user to navigate home.
    """
    return render(request, 'questionbox/home.html')

def ask_question(request):
    """
    Allows user to ask a question. Uses a form.
    """
    if request.method == 'POST':
        form = QuestionForm(data=request.POST)
        if form.is_valid():
            the_question = form.save(commit=False)
            the_question.user = request.user
            the_question.save()
            return redirect(to='view_user_questions')
    else:
        form = QuestionForm()
    
    return render(request, 'questionbox/ask_question.html', {
        'form': form, 
    })

def view_question(request, question_pk):
    """
    Shows individual questions, their related answers, and offers the option to add an answer.
    """
    question = get_object_or_404(request.user.questions, pk=question_pk)
    return render(request, 'questionbox/view_question.html', {'question': question})

def view_user_questions(request):
    """
    Shows all questions asked by a user with links to open and show the show_question page.
    """
    questions = Question.objects.all()
    return render(request, 'questionbox/view_user_questions.html', {"questions": questions})

def delete_question(request, question_pk):
    """
    Delete a question.
    """
    question = get_object_or_404(request.user.questions, pk=question_pk)

    if request.method == 'POST':
        question.delete()
        return redirect(to='view_user_questions')
    
    return render(request, 'questionbox/delete_question.html', {'question': question})

    
