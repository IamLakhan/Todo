from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length = 500)
    description = models.TextField()
    is_done = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
    # class Meta:
    #     order_with_respect_to = 'user'