from django.db import models
from django.conf import settings


# Create your models here.
class Question(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name="author", on_delete=models.CASCADE)
    question = models.CharField(max_length=50, null=True, blank=True)
    answer = models.CharField(max_length=50, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True, editable=False)


class Quiz(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name="Quiz_author", on_delete=models.CASCADE)
    # section1
    title = models.CharField(max_length=20, null=True, blank=True)
    numberQuestions = models.IntegerField(null=True, blank=True, default=0)
    question1 = models.CharField(max_length=100, null=True, blank=True, default='')
    answer1 = models.CharField(max_length=100, null=True, blank=True, default='')
    question2 = models.CharField(max_length=100, null=True, blank=True, default='')
    answer2 = models.CharField(max_length=100, null=True, blank=True, default='')
    question3 = models.CharField(max_length=100, null=True, blank=True, default='')
    answer3 = models.CharField(max_length=100, null=True, blank=True, default='')
    question4 = models.CharField(max_length=100, null=True, blank=True, default='')
    answer4 = models.CharField(max_length=100, null=True, blank=True, default='')
    question5 = models.CharField(max_length=100, null=True, blank=True, default='')
    answer5 = models.CharField(max_length=100, null=True, blank=True, default='')
    # section 2
    attachImage = models.FileField(upload_to='media/coverPhoto/attachImage')

    timestamp = models.DateTimeField(auto_now_add=True, editable=False)
    start_date = models.DateTimeField(null=True, blank=True)
    end_date = models.DateTimeField(null=True, blank=True)
    duration = models.CharField(max_length=20, null=True, blank=True)

    # section 5 reward
    cashReward = models.BooleanField(default=False)
    physicalReward = models.BooleanField(default=False)
    select_winner = models.IntegerField(default=1, null=True, blank=True)  # number of winners to reward

    cashPrize = models.BigIntegerField(default=0, null=True, blank=True)  # reward amount
    worth = models.BigIntegerField(default=0, null=True, blank=True)
    otherBenefit = models.CharField(max_length=500, null=True, blank=True)
    # Challenge Status
    approved = models.BooleanField(default=False)
    rejected = models.BooleanField(default=False)
    draft = models.BooleanField(default=False)
    pending = models.BooleanField(default=False)
    active = models.BooleanField(default=False)
    closed = models.BooleanField(default=False)

    # Payment Status
    payin = models.BooleanField(default=False)
    payout = models.BooleanField(default=False)
    payoutFailed = models.BooleanField(default=False)
    payinFailed = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.title}'
