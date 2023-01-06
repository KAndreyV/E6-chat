from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Writer(User):
    avatar = models.ImageField(upload_to='images/', default=None)
    # chats = models.ManyToManyField(Chat)

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse('user_detail', args=[str(self.id)])


class Chat(models.Model):
    name = models.CharField(max_length=77)
    time_in = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, related_name='chats', on_delete=models.CASCADE)


class Message(models.Model):
    message = models.JSONField()
    user = models.ForeignKey(to=Writer, on_delete=models.CASCADE, null=True, blank=True)
    