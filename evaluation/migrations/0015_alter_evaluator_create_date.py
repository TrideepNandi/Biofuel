# Generated by Django 4.0.1 on 2022-02-25 02:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evaluation', '0014_alter_evaluator_create_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evaluator',
            name='create_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
