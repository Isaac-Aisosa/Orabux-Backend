from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


# Create user token when signup or login.

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


# Create user Profile model.
class UserProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, related_name="user", on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null=True, blank=True)
    bio = models.CharField(max_length=100, null=True, blank=True)
    profession = models.CharField(max_length=100, null=True, blank=True)
    location = models.CharField(max_length=200, null=True, blank=True)
    DOB = models.CharField(max_length=5, blank=True, null=True)
    Gender = models.CharField(max_length=7, blank=True, null=True)
    Phone = models.CharField(max_length=20, blank=True, null=True)
    profileImage = models.ImageField(verbose_name='Profile Image',
                                     upload_to='media/profile_images', blank=True, null=True)
    avaterImage = models.ImageField(verbose_name='Avater Image', upload_to='media/avater_image',
                                    null=True, blank=True)
    follower = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="userFollower", blank=True)
    following = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="userFollowing", blank=True)
    joined = models.DateTimeField(auto_now_add=True, editable=False)

    def __str__(self):
        return f'{self.user} Profile'


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_user_account(sender, instance=None, created=False, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)


# Create user Profile model.
class EmailVerification(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, related_name="userEmail", on_delete=models.CASCADE)
    email = models.EmailField(blank=True, null=True)
    code = models.CharField(max_length=7, blank=True, null=True)
    status = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user} EmailVerification'


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_user_account(sender, instance=None, created=False, **kwargs):
    if created:
        EmailVerification.objects.create(user=instance)
