# Generated by Django 4.0.1 on 2022-09-29 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0173_alter_lead_confirm_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lead',
            name='confirm_code',
            field=models.CharField(default='816545757250', max_length=50),
        ),
    ]
