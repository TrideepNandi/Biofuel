# Generated by Django 4.0.1 on 2022-04-04 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0074_alter_lead_confirm_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lead',
            name='confirm_code',
            field=models.CharField(default='610170557267', max_length=50),
        ),
    ]