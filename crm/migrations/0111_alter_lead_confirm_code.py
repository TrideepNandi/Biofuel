# Generated by Django 4.0.1 on 2022-05-13 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0110_alter_lead_confirm_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lead',
            name='confirm_code',
            field=models.CharField(default='101550818583', max_length=50),
        ),
    ]
