# Generated by Django 4.0.1 on 2023-04-21 09:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('evaluation', '0105_alter_evaluator_biofuel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evalebelstatement',
            name='evalebel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='elabelstatement', to='evaluation.evalabel'),
        ),
    ]
