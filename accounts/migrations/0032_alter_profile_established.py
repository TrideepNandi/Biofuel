# Generated by Django 4.0.1 on 2022-07-28 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0031_usertype_is_marine'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='established',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]