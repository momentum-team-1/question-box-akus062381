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
    favorited_by = models.ManyToManyField(to=User, related_name='favorite_questions')

    # def __str__(self):
    #     return self.question_title


class Answer(models.Model):
    question = models.ForeignKey(to=Question, on_delete=models.CASCADE, related_name="answers")
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name="answers")
    answer_text = models.TextField(max_length=1000, blank=True, null=True)
    date_field = models.DateTimeField(auto_now_add=True)
    correct_answer = models.BooleanField(default=False)
    favorited_by = models.ManyToManyField(to=User, related_name='favorite_answers')
    marked_correct = models.BooleanField(default=False)

    def is_marked_correct(self, answer):
        return self.marked_correct.filter(pk=answer.pk).count() == 1




    