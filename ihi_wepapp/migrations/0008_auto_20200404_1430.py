# Generated by Django 2.2.3 on 2020-04-04 14:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ihi_wepapp', '0007_aboutcovid19_covid19guidlines_covid19howtostaysafe_covid19notice_covid19stats'),
    ]

    operations = [
        migrations.RenameField(
            model_name='covid19stats',
            old_name='covid_19HowToStaySafe',
            new_name='covid_19Stats',
        ),
    ]