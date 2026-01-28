from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Todo(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='todos')
    title = models.CharField(max_length=255)
    is_complete = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)

    @property
    def truncated_title(self):
        return self.title[:14] + '...' if len(self.title) > 14 else self.title
