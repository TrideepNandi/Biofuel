# Generated by Django 4.0.1 on 2023-04-11 13:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('evaluation', '0104_nextactivities_same_tried_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evaluator',
            name='biofuel',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='eva_fuel', to='evaluation.biofuel'),
        ),
    ]