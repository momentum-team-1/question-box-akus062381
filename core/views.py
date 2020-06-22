from django.shortcuts import render, redirect, get_object_or_404
from .models import Question, Answer
from .forms import QuestionForm, AnswerForm
from django.db.models import Q
from users.models import User
from django.contrib.auth.decorators import login_required
from .forms import MyUserCreationForm, MyUserChangeForm
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt



# Create your views here.

def home(request):
    """
    Allows user to navigate home, where they can view all questions by all users.
    """
    questions = Question.objects.all()
    return render(request, 'questionbox/home.html', {"questions": questions})

@login_required
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
    # questions = Question.objects.filter()
    question = get_object_or_404(Question.objects.all(), pk=question_pk)
    is_user_favorite = False
    if request.user.is_authenticated:
        is_user_favorite = request.user.is_favorite_question(question)

    answer_form = AnswerForm()
    return render(request, 'questionbox/view_question.html', {
        'question': question, 
        'answer_form': answer_form,
        'is_user_favorite': is_user_favorite,
    })

@login_required
@csrf_exempt
def add_favorite_question(request, question_pk):
    question = get_object_or_404(Question.objects.all(), pk=question_pk)

    if request.user.is_favorite_question(question):
        request.user.favorite_questions.remove(question)
        return JsonResponse({"isFavorite": False})
    else:
        request.user.favorite_questions.add(question)
        return JsonResponse({"isFavorite": True})

@login_required
def view_user_questions(request):
    """
    Shows all questions asked by a user with links to open and show the show_question page.
    """
    questions = Question.objects.filter(user=request.user)
    return render(request, 'questionbox/view_user_questions.html', {
        "questions": questions
    })

@login_required
def delete_question(request, question_pk):
    """
    Delete a question.
    """
    question = get_object_or_404(request.user.questions, pk=question_pk)

    if request.method == 'POST':
        question.delete()
        return redirect(to='view_user_questions')
    
    return render(request, 'questionbox/delete_question.html', {
        'question': question
    })

@login_required
def add_answer(request, question_pk):
    """
    Adds an answer to an existing question and appends it at the end of any already existing answers.
    """
    question = get_object_or_404(request.user.questions, pk=question_pk)

    if request.method == 'POST':
        form = AnswerForm(data=request.POST)
        if form.is_valid():
            the_answer = form.save(commit=False)
            the_answer.question = question
            the_answer.user = request.user
            the_answer.save()
            return redirect(to='view_question', question_pk=question.pk)
    else:
        form = AnswerForm()
    
    return render(request, 'questionbox/add_answer.html', {
        'answer_form': form, 
        'question': question
    })

def search_questions(request):
    query = request.GET.get('q')

    if query is not None:
        results = Question.objects.filter(Q(question_body__icontains=query) | Q(question_title__icontains=query)) 
        answers = Answer.objects.filter(Q(answer_text__icontains=query))
    else:
        results = None
        answers = None
    
    return render(request, 'questionbox/search_questions.html', {
        'query': query,
        'results': results,
        'answers': answers,
    })

@login_required
def profile_view(request, username):
    profile = User.objects.get(username=username)

    if request.method == 'POST':
        
        form = MyUserChangeForm(instance=profile, data=request.POST, files=request.FILES)
        if form.is_valid():
            user_profile = form.save()
            user_profile.user = request.user
            user_profile.save()
            return redirect(to='profile_view', username=username)
    else:
        form = MyUserChangeForm(instance=profile)
    
    return render(request, 'questionbox/profile_view.html', {"profile": profile, "form": form})



