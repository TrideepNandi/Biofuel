# Generated by Django 4.0.1 on 2023-08-31 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0264_alter_lead_confirm_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lead',
            name='confirm_code',
            field=models.CharField(default='600910107186', max_length=50),
        ),
    ]