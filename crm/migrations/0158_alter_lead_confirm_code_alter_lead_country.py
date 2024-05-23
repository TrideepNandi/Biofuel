# Generated by Django 4.0.1 on 2022-09-06 12:23

from django.db import migrations, models
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0157_alter_lead_address_1_alter_lead_address_2_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lead',
            name='confirm_code',
            field=models.CharField(default='361495015353', max_length=50),
        ),
        migrations.AlterField(
            model_name='lead',
            name='country',
            field=django_countries.fields.CountryField(blank=True, max_length=2, null=True),
        ),
    ]
