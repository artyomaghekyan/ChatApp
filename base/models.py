from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class ChatRoom(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    date = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ('date',)

    def __str__(self) -> str:
        return self.name
    
class ChatMessages(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(ChatRoom, on_delete=models.CASCADE)
    message_content = models.TextField()
    date = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.message_content

    class Meta:
        ordering = ('date',)

