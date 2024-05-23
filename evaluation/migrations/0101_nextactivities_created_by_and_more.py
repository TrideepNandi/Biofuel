# Generated by Django 4.0.1 on 2023-03-14 09:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('evaluation', '0100_alter_nextactivities_compulsory_questions_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='nextactivities',
            name='created_by',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='serviceby', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='nextactivities',
            name='compulsory_questions',
            field=models.ManyToManyField(help_text='Allow multiple. The selected options should be highlighted.', limit_choices_to={'is_active': True}, related_name='compulsory_next', to='evaluation.Question', verbose_name='Please select compulsory questions'),
        ),
        migrations.AlterField(
            model_name='nextactivities',
            name='related_questions',
            field=models.ManyToManyField(help_text='Allow multiple option selection. The selected options should be highlighted.', limit_choices_to={'is_active': True}, related_name='related_next', to='evaluation.Question', verbose_name='Please select related questions'),
        ),
    ]
