# Generated by Django 4.0.1 on 2023-09-21 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0267_alter_lead_confirm_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lead',
            name='confirm_code',
            field=models.CharField(default='808886772025', max_length=50),
        ),
    ]