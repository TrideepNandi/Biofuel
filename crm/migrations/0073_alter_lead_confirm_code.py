# Generated by Django 4.0.1 on 2022-04-02 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0072_alter_lead_confirm_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lead',
            name='confirm_code',
            field=models.CharField(default='328410225490', max_length=50),
        ),
    ]
