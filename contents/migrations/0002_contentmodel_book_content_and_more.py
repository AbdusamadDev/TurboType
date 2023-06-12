# Generated by Django 4.2.2 on 2023-06-10 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contents', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contentmodel',
            name='book_content',
            field=models.TextField(default='asd', max_length=5000),
        ),
        migrations.AlterField(
            model_name='contentmodel',
            name='book_page',
            field=models.PositiveIntegerField(default=0),
        ),
    ]