# Generated by Django 4.0.1 on 2022-03-30 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0054_alter_lead_confirm_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lead',
            name='confirm_code',
            field=models.CharField(default='713897071314', max_length=50),
        ),
    ]
