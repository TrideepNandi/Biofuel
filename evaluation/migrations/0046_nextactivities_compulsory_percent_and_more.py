# Generated by Django 4.0.1 on 2022-05-09 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evaluation', '0045_evalebelstatement_next_activity'),
    ]

    operations = [
        migrations.AddField(
            model_name='nextactivities',
            name='compulsory_percent',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='nextactivities',
            name='related_percent',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='nextactivities',
            name='short_description',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='nextactivities',
            name='url',
            field=models.URLField(default=''),
            preserve_default=False,
        ),
    ]
