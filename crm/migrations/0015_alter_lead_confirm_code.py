# Generated by Django 4.0.1 on 2022-02-25 02:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0014_alter_lead_confirm_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lead',
            name='confirm_code',
            field=models.CharField(default='278931680973', max_length=50),
        ),
    ]