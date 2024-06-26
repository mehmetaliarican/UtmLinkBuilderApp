# Generated by Django 4.2.13 on 2024-06-19 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WebCampaignUrl',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('website_url', models.CharField(max_length=100)),
                ('utm_id', models.CharField(blank=True, max_length=100, null=True)),
                ('utm_source', models.CharField(max_length=100)),
                ('utm_medium', models.CharField(max_length=100)),
                ('utm_campaign', models.CharField(blank=True, max_length=100, null=True)),
                ('utm_term', models.CharField(blank=True, max_length=100, null=True)),
                ('utm_content', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'verbose_name': 'WebCampaignUrl',
                'verbose_name_plural': 'WebCampaignUrls',
            },
        ),
    ]
