from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Notes(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)  #value is automatically populated each time
    # FK, when user is deleted - the associated notes are deleted.
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notes')
    is_public = models.BooleanField(default=False)
