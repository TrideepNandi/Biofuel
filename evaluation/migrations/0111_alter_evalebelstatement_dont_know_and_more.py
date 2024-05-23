# Generated by Django 4.0.1 on 2023-06-02 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evaluation', '0110_alter_evaluator_slug_alter_evaluator_stdoil_key'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evalebelstatement',
            name='dont_know',
            field=models.BooleanField(db_index=True, default=False),
        ),
        migrations.AlterField(
            model_name='evalebelstatement',
            name='positive',
            field=models.CharField(db_index=True, default=0, max_length=1),
        ),
        migrations.AlterField(
            model_name='nextactivities',
            name='compulsory_questions',
            field=models.ManyToManyField(db_index=True, help_text='Allow multiple. The selected options should be highlighted.', limit_choices_to={'is_active': True}, related_name='compulsory_next', to='evaluation.Question', verbose_name='Please select compulsory questions to be answered by the test'),
        ),
        migrations.AlterField(
            model_name='nextactivities',
            name='related_questions',
            field=models.ManyToManyField(db_index=True, help_text='Allow multiple option selection. The selected options should be highlighted.', limit_choices_to={'is_active': True}, related_name='related_next', to='evaluation.Question', verbose_name='Please select related questions to be answered by the test'),
        ),
    ]