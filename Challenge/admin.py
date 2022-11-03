from django.contrib import admin
from .models import *


# Register your models here.

class ChallengeAdmin(admin.ModelAdmin):
    list_display = ("title", "user", "type", "voter", "duration", "cashReward", "worth", "draft", "approved")


admin.site.register(Challenge, ChallengeAdmin)

admin.site.register(ChallengeMinimumVote)