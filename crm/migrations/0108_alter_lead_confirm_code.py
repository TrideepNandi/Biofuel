# Generated by Django 4.0.1 on 2022-05-13 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0107_alter_lead_confirm_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lead',
            name='confirm_code',
            field=models.CharField(default='844951203527', max_length=50),
        ),
    ]
