from django.contrib import admin
from .models import *


# Register your models
#
#
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "name", "Gender", "Phone", "joined")


admin.site.register(UserProfile, UserProfileAdmin)


class EmailVerificationAdmin(admin.ModelAdmin):
    list_display = ("user", "email", "code", "status")


admin.site.register(EmailVerification, EmailVerificationAdmin)
