# Generated by Django 2.1.15 on 2020-11-28 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ihi_wepapp', '0015_auto_20201128_1204'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='video_file',
            field=models.URLField(blank=True, null=True),
        ),
    ]
