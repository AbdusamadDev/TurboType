from django.db import models
from django.contrib.auth.models import User


<<<<<<< HEAD
# Create your models here.

class Feedback(models.Model):
    user_id = models.ForeignKey(to=User, on_delete=models.CASCADE)
    feedback = models.CharField(max_length=200,blank=False)
    date = models.DateField()
=======
class FeedbackModel(models.Model):
    pass
>>>>>>> b76fcb9a0111a77b80b50cfd58036a0cb043b823
