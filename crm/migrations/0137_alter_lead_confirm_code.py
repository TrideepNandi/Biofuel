# Generated by Django 4.0.1 on 2022-06-20 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0136_alter_lead_confirm_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lead',
            name='confirm_code',
            field=models.CharField(default='948704326547', max_length=50),
        ),
    ]
