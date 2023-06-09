# Generated by Django 4.2.2 on 2023-06-12 10:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(default='uncategorized', max_length=150)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='ContentModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_name', models.CharField(default='Unnamed', max_length=100)),
                ('book_author', models.CharField(default='Unknown', max_length=80)),
                ('book_content', models.TextField(default='asd', max_length=5000)),
                ('book_page', models.PositiveIntegerField(default=0)),
                ('is_confirmed', models.BooleanField(choices=[(1, 'Confirmed'), (0, 'Not confirmed')], default=0)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contents.categorymodel')),
                ('user_id', models.ForeignKey(default=5, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
