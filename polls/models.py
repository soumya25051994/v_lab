from django.db import models
from django.utils import timezone
import datetime

# Create your models here.
class Track(models.Model):
    track_name = models.CharField(max_length=50)
    def __str__(self):
        return self.track_name

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField(blank=True, null=True)
    created_date = models.DateTimeField(default=timezone.now)
    tracker = models.ForeignKey(Track,  default=False, on_delete=models.CASCADE)

    def __str__(self):
        return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

class AnswerValidator(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.ForeignKey(Choice, on_delete=models.CASCADE)




