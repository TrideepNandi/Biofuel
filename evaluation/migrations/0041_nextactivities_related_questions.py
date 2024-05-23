# Generated by Django 4.0.1 on 2022-05-02 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evaluation', '0040_alter_nextactivities_compulsory_questions'),
    ]

    operations = [
        migrations.AddField(
            model_name='nextactivities',
            name='related_questions',
            field=models.ManyToManyField(help_text='Allow multiple option selection. The selected options should be highlighted.', limit_choices_to={'is_active': True}, related_name='related_next', to='evaluation.Question', verbose_name='Please select related questions'),
        ),
    ]