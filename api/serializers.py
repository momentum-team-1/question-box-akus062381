from rest_framework import serializers
from users.models import User
from core.models import Question, Answer

class UserSerializer(serializers.HyperlinkedModelSerializer):
    questions = serializers.PrimaryKeyRelatedField(many=True, queryset=Question.objects.all())
    answers = serializers.PrimaryKeyRelatedField(many=True, queryset=Answer.objects.all())
    
    class Meta:
        model = User
        fields = ['id', 'url', 'username', 'email', 'bio', 'questions', 'answers',]

class AnswerSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()

    class Meta:
        model = Answer
        fields = [
            'user', 'answer_text', 'date_field', 'marked_correct', 'question',
        ]


class QuestionSerializer(serializers.HyperlinkedModelSerializer):
    answers = AnswerSerializer(many=True, read_only=True)
    user = serializers.StringRelatedField()

    # def create(self, validated_data):
    #     answers = validated_data.pop('answers', [])
    #     question = Question.objects.create(**validated_data)
    #     for answer in answers:
    #         question.answers.create(**answer)
    #     return question

    class Meta:
        model = Question
        fields = [
            'url',
            'user',
            'question_title',
            'question_body',
            'favorited_by',
            'answers',
        ]

