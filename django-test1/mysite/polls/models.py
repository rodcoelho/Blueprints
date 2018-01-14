import datetime

from django.db import models
from django.utils import timezone

# Models ( the classes below ) contain the essential fields and behaviors of the data you’re storing
# each class is a table
# each variable is a column name
# each variable holds an instance of a Field class (CharField, DateTimeField, etc)
# note the use of ForeignKey. That tells Django each Choice is related to a single Question.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    # we use models.ForeignKey to tie Choice to Questions table
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
