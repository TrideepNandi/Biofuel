# Generated by Django 4.0.1 on 2023-06-02 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evaluation', '0108_alter_option_dont_know_alter_option_overall_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='logicalstring',
            name='options',
            field=models.ManyToManyField(db_index=True, to='evaluation.Option'),
        ),
        migrations.AlterField(
            model_name='logicalstring',
            name='overall',
            field=models.CharField(db_index=True, default=0, max_length=1),
        ),
        migrations.AlterField(
            model_name='logicalstring',
            name='positive',
            field=models.CharField(db_index=True, default=0, max_length=1),
        ),
        migrations.AlterField(
            model_name='optionset',
            name='option_list',
            field=models.CharField(db_index=True, max_length=252, unique=True),
        ),
        migrations.AlterField(
            model_name='optionset',
            name='overall',
            field=models.CharField(db_index=True, default=0, max_length=1),
        ),
        migrations.AlterField(
            model_name='optionset',
            name='positive',
            field=models.CharField(db_index=True, default=0, max_length=1),
        ),
    ]
