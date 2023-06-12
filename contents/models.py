from django.db import models
from django.contrib.auth.models import User
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