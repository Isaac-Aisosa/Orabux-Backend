# from django.db import models
# from django.conf import settings
#
#
# # Create your models here.
# class Conditions(models.Model):
#     condition = models.CharField(max_length=50, null=True, blank=True)
#
#     timestamp = models.DateTimeField(auto_now_add=True, editable=False)
#
#
# class Giveaway(models.Model):
#     user = models.ForeignKey(
#         settings.AUTH_USER_MODEL, related_name="giveaway", on_delete=models.CASCADE)
#     # section1
#     caption = models.CharField(max_length=50, null=True, blank=True)
#     condition = models.ForeignKey(Conditions, related_name="quiz_question", on_delete=models.CASCADE) # condition to win giveaway
#     # section 2
#     attachImage = models.FileField(upload_to='media/giveaway/attachImage')
#
#     timestamp = models.DateTimeField(auto_now_add=True, editable=False)
#     start_date = models.DateTimeField(null=True, blank=True)
#     end_date = models.DateTimeField(null=True, blank=True)
#     duration = models.CharField(max_length=20, null=True, blank=True)
#
#     # section 5 reward
#     cashReward = models.BooleanField(default=False)
#     physicalReward = models.BooleanField(default=False)
#     select_winner = models.IntegerField(default=0, null=True, blank=True)  # number of winners to reward
#
#     cashPrize = models.BigIntegerField(default=0, null=True, blank=True)  # reward amount
#     worth = models.BigIntegerField(default=0, null=True, blank=True)
#     otherBenefit = models.CharField(max_length=500, null=True, blank=True)
#     # Challenge Status
#     approved = models.BooleanField(default=False)
#     rejected = models.BooleanField(default=False)
#     draft = models.BooleanField(default=False)
#     pending = models.BooleanField(default=False)
#     active = models.BooleanField(default=False)
#     closed = models.BooleanField(default=False)
#
#     # Payment Status
#     payin = models.BooleanField(default=False)
#     payout = models.BooleanField(default=False)
#     payoutFailed = models.BooleanField(default=False)
#     payinFailed = models.BooleanField(default=False)
#
#     def __str__(self):
#         return f'{self.title}'
