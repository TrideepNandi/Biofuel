# Generated by Django 4.0.1 on 2022-03-22 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0027_alter_lead_confirm_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lead',
            name='confirm_code',
            field=models.CharField(default='080668454539', max_length=50),
        ),
    ]