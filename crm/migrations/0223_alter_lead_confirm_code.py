# Generated by Django 4.0.1 on 2022-12-07 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0222_alter_lead_confirm_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lead',
            name='confirm_code',
            field=models.CharField(default='558668009944', max_length=50),
        ),
    ]
