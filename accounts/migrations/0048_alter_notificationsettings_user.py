# Generated by Django 4.0.1 on 2023-10-20 09:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0047_alter_notificationsettings_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notificationsettings',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='notificationsettings', serialize=False, to=settings.AUTH_USER_MODEL),
        ),
    ]
