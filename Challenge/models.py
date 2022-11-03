from django.conf import settings
from django.db import models


# Create your models here.

class ChallengeType(models.Model):
    type = models.CharField(max_length=20, null=True, blank=True, )
    timestamp = models.DateTimeField(auto_now_add=True, editable=False)

    def __str__(self):
        return f'{self.type} challenge'


class ChallengeMinimumVote(models.Model):
    value = models.BigIntegerField(null=True, blank=True)
    active = models.BooleanField(True)

    def __str__(self):
        return f'{self.value}'


class Reward(models.Model):
    reward = models.CharField(max_length=30, null=True, blank=True)

    active = models.BooleanField(True)

    def __str__(self):
        return f'{self.reward}'


allowed_Voter = (
    ("public", "public"),
    ("followers", "followers"),
    ("selected", "selected"),
)


class Challenge(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name="challenge_creator", on_delete=models.CASCADE)
    # section1
    title = models.CharField(max_length=20, null=True, blank=True)
    description = models.CharField(max_length=500, null=True, blank=True)
    type = models.CharField(max_length=30, null=True, blank=True)
    # section 2
    attachVideo = models.FileField(upload_to='media/challenge/attachVideo')
    attachAudio = models.FileField(upload_to='media/challenge/attachAudio')
    attachImage = models.FileField(upload_to='media/challenge/attachImage')
    # section 3
    voter = models.CharField(max_length=150, choices=allowed_Voter, default="public")
    minimumVote = models.BigIntegerField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True, editable=False)
    start_date = models.DateTimeField(null=True, blank=True)
    end_date = models.DateTimeField(null=True, blank=True)
    duration = models.CharField(max_length=20, null=True, blank=True)

    # section 5 reward
    cashReward = models.BooleanField(default=False)
    physicalReward = models.BooleanField(default=False)
    select_winner = models.IntegerField(default=0, null=True, blank=True)  # number of winners to reward

    first_place_reward = models.BigIntegerField(default=0, null=True, blank=True)  # first place reward amount
    second_place_reward = models.BigIntegerField(default=0, null=True, blank=True)  # second place reward amount
    third_place_reward = models.BigIntegerField(default=0, null=True, blank=True)  # third place reward amount
    forth_place_reward = models.BigIntegerField(default=0, null=True, blank=True)  # forth place reward amount
    firth_place_reward = models.BigIntegerField(default=0, null=True, blank=True)
    six_place_reward = models.BigIntegerField(default=0, null=True, blank=True)
    seven_place_reward = models.BigIntegerField(default=0, null=True, blank=True)
    eight_place_reward = models.BigIntegerField(default=0, null=True, blank=True)
    ninth_place_reward = models.BigIntegerField(default=0, null=True, blank=True)
    tenth_place_reward = models.BigIntegerField(default=0, null=True, blank=True)

    others_reward = models.BigIntegerField(default=0, null=True, blank=True)  # others below 3rd place reward amount
    others_share_ratio = models.IntegerField(default=0, null=True, blank=True)  # sharing ratio for selected winner below 3rd place

    worth = models.BigIntegerField(default=0, null=True, blank=True)
    otherReward = models.CharField(max_length=500, null=True, blank=True)
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


class JoinChallenge(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name="contestant", on_delete=models.CASCADE)
    challenge = models.ForeignKey(Challenge, related_name="challenge", on_delete=models.CASCADE)
    video = models.FileField(upload_to=f'media/challenge/{Challenge}/Video')
    vote = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="voters", blank=True)
    timestamp = models.DateTimeField(auto_now_add=True, editable=False)

    def __str__(self):
        return f'{self.user} challenge'
