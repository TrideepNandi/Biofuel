# Generated by Django 4.0.1 on 2022-02-24 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0006_alter_lead_confirm_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lead',
            name='confirm_code',
            field=models.CharField(default='206515570749', max_length=50),
        ),
    ]