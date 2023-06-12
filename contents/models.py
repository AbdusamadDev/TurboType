from django.db import models
from django.contrib.auth.models import User
<<<<<<< HEAD
# Create your models here.


class Contents(models.Model):
    user_id = models.ForeignKey(to=User, on_delete=models.CASCADE)
    book_name = models.CharField(max_length=200)
    book_author = models.CharField(max_length=200)
    book_gape = models.URLField(blank=True)
    date_created = models.DateField()
    is_confirned = models.IntegerField() 
    

    def __str__(self):
        return self.book_name
=======

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
>>>>>>> b76fcb9a0111a77b80b50cfd58036a0cb043b823
