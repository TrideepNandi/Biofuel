# Generated by Django 4.0.1 on 2022-04-16 13:07

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('evaluation', '0036_question_chapter_name'),
        ('home', '0002_timeunit'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quotation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_provider', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, parent_link=True, related_name='quotationserviceprovider', to=settings.AUTH_USER_MODEL)),
                ('price', models.DecimalField(decimal_places=2, help_text='Help text will go here', max_digits=10, verbose_name='Quotation Price')),
                ('needy_time', models.IntegerField(help_text='Help Text will go', verbose_name='Total needed time for the test')),
                ('sample_amount', models.IntegerField(help_text='Help Text will go here', verbose_name='Sample amount needed for test')),
                ('factory_pickup', models.BooleanField(help_text='Help Text will go', verbose_name='Factory Sample pick-up')),
                ('test_for', models.CharField(default='Question as above', help_text='Help Text will go here', max_length=252, verbose_name='Tests for question')),
                ('quotation_format', models.FileField(help_text="Only '.pdf' are allowed", upload_to='quotation', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf'])], verbose_name='Upload Quotation (pdf)')),
                ('needy_time_unit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='timeunitquatation', to='home.timeunit', verbose_name='Time Unit')),
                ('price_unit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='priceunitquatation', to='home.priceunit', verbose_name='Price Unit')),
                ('related_questions', models.ForeignKey(help_text='Help Text will go here', on_delete=django.db.models.deletion.CASCADE, to='evaluation.question', verbose_name='Please select all other question which are also tested within the provided quotation')),
                ('require_documents', models.ForeignKey(help_text='Help Text will go', on_delete=django.db.models.deletion.CASCADE, related_name='requiredocuments', to='home.quotationdoctype', verbose_name='Document needed for test')),
                ('sample_amount_unit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='weightunitquatation', to='home.weightunit', verbose_name='Weight Unit')),
            ],
        ),
    ]
