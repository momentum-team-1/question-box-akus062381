from django import forms
from .models import Question
from .models import Answer


class QuestionForm(forms.ModelForm):
    
    class Meta:
        model = Question
        fields = [
            'question_title',
            'question_body',
        ]


class AnswerForm(forms.ModelForm):

    class Meta:
        model = Answer
        fields = [
            'answer_text',
        ]