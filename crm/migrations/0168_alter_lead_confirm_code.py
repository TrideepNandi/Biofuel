# Generated by Django 4.0.1 on 2022-09-29 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0167_alter_lead_confirm_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lead',
            name='confirm_code',
            field=models.CharField(default='665815671848', max_length=50),
        ),
    ]