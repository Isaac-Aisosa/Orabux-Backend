from django.conf import settings
from django.db import models


# Create your models here.

class Post(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name="user_video_post", on_delete=models.CASCADE)
    file = models.FileField(verbose_name='Post', upload_to='media/Post_Files')
    caption = models.CharField(verbose_name='Write a caption..', max_length=500, null=True, blank=True, )
    type = models.CharField(max_length=10, null=True, blank=True, )
    like = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True)
    share = models.BigIntegerField(default=0, null=True, blank=True, )
    timestamp = models.DateTimeField(auto_now_add=True, editable=False)

    def __str__(self):
        return f'{self.user} Post '


class Comment(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name="comment_author", on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name="comment_post", on_delete=models.CASCADE)
    comment = models.CharField(max_length=225, verbose_name='comment')
    timestamp = models.DateTimeField(auto_now_add=True, editable=False)

    def __str__(self):
        return f'{self.post} Comment '
