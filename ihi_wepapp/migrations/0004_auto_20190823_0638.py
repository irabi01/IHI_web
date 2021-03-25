# Generated by Django 2.2.3 on 2019-08-23 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ihi_wepapp', '0003_blog_calls_ced_collaboratinginstitutions_events_funndingpartners_governance_innovationhub_jobs_news_'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blog',
            options={'verbose_name_plural': 'Blogs List'},
        ),
        migrations.AlterModelOptions(
            name='calls',
            options={'verbose_name_plural': 'Calls List'},
        ),
        migrations.AlterModelOptions(
            name='governance',
            options={'verbose_name_plural': 'Governance List'},
        ),
        migrations.AlterModelOptions(
            name='jobs',
            options={'verbose_name_plural': 'Jobs List'},
        ),
        migrations.AlterModelOptions(
            name='news',
            options={'verbose_name_plural': 'News List'},
        ),
        migrations.AlterModelOptions(
            name='opportunity',
            options={'verbose_name_plural': 'Opportunity List'},
        ),
        migrations.AlterModelOptions(
            name='projects',
            options={'verbose_name_plural': 'Projects List'},
        ),
        migrations.AlterModelOptions(
            name='publications',
            options={'verbose_name_plural': 'Publications List'},
        ),
        migrations.AlterModelOptions(
            name='staffs',
            options={'verbose_name_plural': 'Staffs List'},
        ),
        migrations.RenameField(
            model_name='news',
            old_name='uploaded_date',
            new_name='date',
        ),
        migrations.RenameField(
            model_name='projects',
            old_name='funder',
            new_name='funding_partner',
        ),
        migrations.AlterField(
            model_name='governance',
            name='governance1',
            field=models.CharField(choices=[('', 'select governance'), ('BOG', 'Board of Governors'), ('BOT', 'Board of Trustees'), ('MC', 'Management Committee')], max_length=50),
        ),
    ]