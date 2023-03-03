from django.db import models
import datetime

from django.utils import timezone


# learning 2
class Question(models.Model):
    # ...exit
    def __str__(self):
        return self.question_text

    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    # ...q = Question.objects.get(pk=1)
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


# learning 2
class Choice(models.Model):
    # ...
    def __str__(self):
        return self.choice_text

    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
