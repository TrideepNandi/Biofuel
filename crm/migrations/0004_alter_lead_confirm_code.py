# Generated by Django 4.0 on 2024-05-23 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0003_alter_lead_confirm_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lead',
            name='confirm_code',
            field=models.CharField(default='539714559873', max_length=50),
        ),
    ]