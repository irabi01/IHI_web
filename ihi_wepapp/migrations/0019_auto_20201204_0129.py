# Generated by Django 2.1.15 on 2020-12-03 22:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ihi_wepapp', '0018_news_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='slug',
            field=models.SlugField(blank=True, max_length=500),
        ),
    ]