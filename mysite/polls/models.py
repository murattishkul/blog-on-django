from django.db import models
import datetime
from django.utils import timezone
# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length=200) #question text
    pub_date =  models.DateTimeField('date published') #date
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    def __str__(self):
        return self.question_text

class Choice(models.Model):
    choice_text = models.CharField(max_length=200) #choice text
    vote = models.IntegerField(default=0) #number of votes
    question = models.ForeignKey(Question, on_delete=models.CASCADE) #link to some question object

    def __str__(self):
        return self.choice_text
