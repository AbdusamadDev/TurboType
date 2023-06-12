from django.contrib.auth.models import User
from django.db import models

STATUS_CHOICES = (
    (1, 'Confirmed'),
    (0, 'Not confirmed'),
)


class CategoryModel(models.Model):
    category = models.CharField(max_length=150, null=False, blank=False, default="uncategorized")
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.category


class ContentModel(models.Model):
    user_id = models.ForeignKey(to=User, on_delete=models.CASCADE, default=5)
    book_name = models.CharField(max_length=100, unique=False, blank=False, default="Unnamed")
    book_author = models.CharField(max_length=80, unique=False, blank=False, default="Unknown")
    book_content = models.TextField(max_length=5000, blank=False, null=False, default="asd")
    book_page = models.PositiveIntegerField(default=0, blank=False, unique=False)
    category = models.ForeignKey(to=CategoryModel, on_delete=models.CASCADE)
    is_confirmed = models.BooleanField(choices=STATUS_CHOICES, unique=False, default=0)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.book_name
