from django.urls import path
from pollsapp import routers

from . import views
from . import api

router = routers.SharedAPIRootRouter()
router.register(r'questions', api.QuesViewSet)
router.register(r'choices', api.ChoiceViewSet)
router.register(r'tracks', api.TrackViewSet)
router.register(r'questions/track', api.getQuestionsByTrack, basename='get_questions')
router.register(r'getAnswers', api.AnswerValidatorViewSet)
router.register(r'getAnswerStat', api.getAnswerStat, basename='get_AnswerStat')


urlpatterns = [
    path('', views.index, name='index'),
]
