# Generated by Django 5.0.6 on 2024-06-18 21:08

import django.core.validators
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('surname', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=200)),
                ('mobile', models.CharField(blank=True, max_length=17, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')])),
                ('landline', models.CharField(blank=True, max_length=17, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')])),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('isHandled', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Contact Request',
                'verbose_name_plural': 'Contact Requests',
            },
        ),
    ]