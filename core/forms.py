from django import forms
from .models import Question
from .models import Answer
from users.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm



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

class ProfileEditForm(forms.ModelForm):

    class Meta:
        model = User
        fields = (
            'image',
            'current_city',
            'bio',
        )

    
class MyUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = User
        fields = (
            'username',
            'image',
            'current_city',
            'bio',
        )

class MyUserChangeForm(UserChangeForm):

    class Meta(UserChangeForm):
        model = User
        fields = (
            'image',
            'current_city',
            'bio',
        )

