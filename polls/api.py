from django.conf.urls import url, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Question, Choice, Track, AnswerValidator

class QuesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ('id', 'question_text', 'tracker')

class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = ('id', 'question', 'choice_text', 'votes')

class TrackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Track
        fields = ('id', 'track_name')

class AnswerValidatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnswerValidator
        fields = ('question', 'answer')

class QuesViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuesSerializer

class ChoiceViewSet(viewsets.ModelViewSet):
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer

class TrackViewSet(viewsets.ModelViewSet):
    queryset = Track.objects.all()
    serializer_class = TrackSerializer

class AnswerValidatorViewSet(viewsets.ModelViewSet):
    queryset = AnswerValidator.objects.all()
    serializer_class = AnswerValidatorSerializer

class getQuestionsByTrack(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuesSerializer
    lookup_field = 'tracker_id'

    @action(detail=True)
    def date_list(self, request, *args, **kwargs):
        tracker_id = kwargs.get('tracker_id', None)
        req_questions = Question.objects.filter(tracker=tracker_id)
        schedule_json = QuesSerializer(req_questions, many=True)
        return Response(schedule_json.data)

class getAnswerStat(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuesSerializer
    lookup_field = 'question_id'

    @action(detail=True)
    def date_list(self, request, *args, **kwargs):
        q_id = kwargs.get('question_id', None)
        validator_object = AnswerValidator.objects.get(question=q_id)
        ansewr_text = getattr(validator_object, 'answer')
        choices_object = Choice.objects.filter(question=q_id)
        all_votes = 0
        for obj in choices_object:
            vote = getattr(obj, 'votes')
            all_votes += vote
        answer_object = Choice.objects.get(choice_text=ansewr_text)
        correct_votes = getattr(answer_object, 'votes')
        wrong_votes = all_votes - correct_votes

        data = {}
        data['correct_votes'] = correct_votes
        data['wrong_votes'] = wrong_votes

        return Response(data)
