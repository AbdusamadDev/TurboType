from django.db import models
from django.contrib.auth.models import User

STATUS_CHOICES = (
    (1, 'Confirmed'),
    (0, 'Not confirmed'),
)


class ContentModel(models.Model):
    user_id = models.ForeignKey(to=User, on_delete=models.CASCADE, default=5)
    book_name = models.CharField(max_length=100, unique=False, blank=False, default="Unnamed")
    book_author = models.CharField(max_length=80, unique=False, blank=False, default="Unknown")
    book_content = models.TextField(max_length=5000, blank=False, null=False, default="asd")
    book_page = models.PositiveIntegerField(default=0, blank=False, unique=False)
    is_confirmed = models.BooleanField(choices=STATUS_CHOICES, unique=False, default=0)
    date_created = models.DateTimeField(auto_now_add=True)
