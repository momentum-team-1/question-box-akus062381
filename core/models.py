from django.db import models
from users.models import User

# Create your models here.

class Question(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name="questions")
    question_title = models.CharField(max_length=255, blank=True, null=True)
    question_body = models.TextField(max_length=1000, blank=True, null=True, help_text="Type your question here.")
    date_field = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.question_title


class Answer(models.Model):
    question = models.ForeignKey(to=Question, on_delete=models.CASCADE, related_name="answers")
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name="answers")
    answer_text = models.TextField(max_length=1000, blank=True, null=True)
    date_field = models.DateField(auto_now_add=True)
    correct_answer = models.BooleanField()

    def __str__(self):
        return self.answer_text