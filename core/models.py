from django.db import models
from users.models import User
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.detail import DetailView

# Create your models here.

class Question(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name="questions")
    question_title = models.CharField(max_length=255, blank=True, null=True)
    question_body = models.TextField(max_length=1000, blank=True, null=True, help_text="Type your question here.")
    date_field = models.DateField(auto_now_add=True)

    # def __str__(self):
    #     return self.question_title


class Answer(models.Model):
    question = models.ForeignKey(to=Question, on_delete=models.CASCADE, related_name="answers")
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name="answers")
    answer_text = models.TextField(max_length=1000, blank=True, null=True)
    date_field = models.DateTimeField(auto_now_add=True)
    correct_answer = models.BooleanField(default=False)

    # def __str__(self):
    #     return self.answer_text

def search_questions(search_term):
    questions = get_all_questions(Question.objects)
    return questions.filter(Q(question_title__icontains=search_term)
        | Q(question_body__icontains=search_term))

def get_all_questions(queryset, user):
    if user.is_authenticated:
        questions = queryset.filter(Q(public=True) | Q(user=user))
    else:
        questions = queryset.filter(public=True)
    return questions

# class UserDetailView(LoginRequiredMixin, DetailView):

#     model = User
#     slug_field = 'username'
#     slug_url_kwarg = 'username'
#     template_name = 'questionbox/profile_view.html'

#     def get_profile(self):

#         profile = get_object_or_404(User, username=self.kwargs.get('username'))

#         if self.request.user.username == profile.username:
#             return profile
#         else:
#             print("You are not the owner!")


    