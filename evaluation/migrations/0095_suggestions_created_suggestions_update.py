# Generated by Django 4.0.1 on 2023-02-17 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evaluation', '0094_alter_suggestions_su_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='suggestions',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='suggestions',
            name='update',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
