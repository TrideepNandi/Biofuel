# Generated by Django 4.0.1 on 2022-03-31 09:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('evaluation', '0020_question_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='slug',
        ),
    ]
