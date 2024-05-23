# Generated by Django 4.0.1 on 2022-02-08 10:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('evaluation', '0006_remove_evaluator_creator'),
    ]

    operations = [
        migrations.AddField(
            model_name='evaluator',
            name='creator',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user', to=settings.AUTH_USER_MODEL),
        ),
    ]
