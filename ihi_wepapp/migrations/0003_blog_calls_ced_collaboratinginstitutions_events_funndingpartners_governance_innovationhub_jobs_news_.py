# Generated by Django 2.2.3 on 2019-08-21 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ihi_wepapp', '0002_auto_20190821_1443'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('uploaded_date', models.DateField()),
                ('location', models.CharField(default='Morogoro', max_length=50)),
                ('image', models.FileField(default='settings.MEDIA_ROOT/logos/anonymous.jpg', upload_to='')),
                ('description', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'Blogs Lists',
            },
        ),
        migrations.CreateModel(
            name='Calls',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('call_document', models.FileField(upload_to='')),
            ],
            options={
                'verbose_name_plural': 'Calls Lists',
            },
        ),
        migrations.CreateModel(
            name='CED',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('left_description', models.TextField()),
                ('headline', models.CharField(max_length=200)),
                ('left_headline', models.CharField(max_length=200)),
                ('image', models.FileField(default='settings.MEDIA_ROOT/logos/anonymous.jpg', upload_to='')),
                ('document', models.FileField(default='settings.MEDIA_ROOT/logos/anonymous.jpg', upload_to='')),
                ('left_link', models.URLField(blank=True)),
            ],
            options={
                'verbose_name_plural': 'Chief Executive Director',
            },
        ),
        migrations.CreateModel(
            name='CollaboratingInstitutions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=200)),
                ('link', models.URLField()),
            ],
            options={
                'verbose_name_plural': 'Collaborating Institutions',
            },
        ),
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('caption', models.CharField(max_length=500)),
                ('event_date', models.DateField()),
                ('event_time', models.CharField(max_length=20)),
                ('uploaded_date', models.DateTimeField(auto_now_add=True)),
                ('location', models.CharField(default='Morogoro', max_length=50)),
                ('image', models.FileField(default='settings.MEDIA_ROOT/logos/anonymous.jpg', upload_to='')),
                ('description', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'Events Lists',
            },
        ),
        migrations.CreateModel(
            name='FunndingPartners',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=200)),
                ('link', models.URLField()),
            ],
            options={
                'verbose_name_plural': 'Funnding Partners',
            },
        ),
        migrations.CreateModel(
            name='Governance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(default='settings.MEDIA_ROOT/logos/anonymous.jpg', upload_to='')),
                ('profile_image', models.FileField(default='settings.MEDIA_ROOT/logos/anonymous.jpg', upload_to='')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('headline', models.CharField(default='', max_length=1000)),
                ('governance1', models.CharField(choices=[('', 'select governance'), ('BOG', 'Board of Governors'), ('BOT', 'Board of Trustees'), ('SAC', 'Scientific Advisory Committee'), ('FARC', 'Finance, Audit & Risk Committee'), ('MC', 'Management Committee')], max_length=50)),
                ('email', models.EmailField(default='', max_length=100)),
                ('background_and_education', models.TextField(default='')),
                ('professional_experience_and_skills', models.TextField()),
                ('description', models.TextField(default='')),
                ('publication_link', models.URLField(blank=True)),
            ],
            options={
                'verbose_name_plural': 'Governance Lists',
            },
        ),
        migrations.CreateModel(
            name='InnovationHub',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('uploaded_date', models.DateTimeField(auto_now_add=True)),
                ('description', models.TextField()),
                ('image', models.FileField(default='settings.MEDIA_ROOT/logos/anonymous.jpg', upload_to='')),
            ],
            options={
                'verbose_name_plural': 'Innovation-hub',
            },
        ),
        migrations.CreateModel(
            name='Jobs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('job_document', models.FileField(upload_to='')),
            ],
            options={
                'verbose_name_plural': 'Jobs Lists',
            },
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('caption', models.CharField(max_length=500)),
                ('uploaded_date', models.DateField()),
                ('location', models.CharField(default='Morogoro', max_length=50)),
                ('image', models.FileField(default='settings.MEDIA_ROOT/logos/anonymous.jpg', upload_to='')),
                ('description', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'News Lists',
            },
        ),
        migrations.CreateModel(
            name='Opportunity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('opportunity_document', models.FileField(upload_to='')),
            ],
            options={
                'verbose_name_plural': 'Opportunity Lists',
            },
        ),
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('project_leader', models.CharField(blank=True, max_length=100)),
                ('principal_investigator', models.CharField(blank=True, max_length=100)),
                ('administrator', models.CharField(blank=True, max_length=100)),
                ('funder', models.CharField(blank=True, max_length=200)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('uploaded_date', models.DateTimeField(auto_now_add=True)),
                ('department', models.CharField(choices=[('', 'select department'), ('EH', 'Environmental Health and Ecological Sciences'), ('IC', 'Interventions and Clinical Trials'), ('HS', 'Health Systems, Impact Evaluation and Policy'), ('TC', 'Training & Capacity Building')], max_length=50)),
                ('image', models.FileField(default='settings.MEDIA_ROOT/logos/anonymous.jpg', upload_to='')),
                ('description', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'Projects Lists',
            },
        ),
        migrations.CreateModel(
            name='Publications',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('published_date', models.DateField(blank=True)),
                ('title', models.CharField(max_length=500)),
                ('journal_name', models.CharField(max_length=100)),
                ('authors', models.CharField(default='', max_length=1000)),
                ('website_link', models.CharField(max_length=200)),
                ('abstract', models.TextField(blank=True)),
            ],
            options={
                'verbose_name_plural': 'Publications Lists',
            },
        ),
        migrations.CreateModel(
            name='Staffs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(default='settings.MEDIA_ROOT/logos/anonymous.jpg', upload_to='')),
                ('profile_image', models.FileField(default='settings.MEDIA_ROOT/logos/anonymous.jpg', upload_to='')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('headline', models.CharField(default='', max_length=1000)),
                ('environmental_department', models.CharField(blank=True, choices=[('', 'select department'), ('EH', 'Environmental Health and Ecological Sciences'), ('IC', 'Interventions and Clinical Trials'), ('HS', 'Health Systems, Impact Evaluation and Policy'), ('TC', 'Training & Capacity Building')], default='select department', max_length=50)),
                ('intervention_department', models.CharField(blank=True, choices=[('', 'select department'), ('EH', 'Environmental Health and Ecological Sciences'), ('IC', 'Interventions and Clinical Trials'), ('HS', 'Health Systems, Impact Evaluation and Policy'), ('TC', 'Training & Capacity Building')], default='select department', max_length=50)),
                ('health_department', models.CharField(blank=True, choices=[('', 'select department'), ('EH', 'Environmental Health and Ecological Sciences'), ('IC', 'Interventions and Clinical Trials'), ('HS', 'Health Systems, Impact Evaluation and Policy'), ('TC', 'Training & Capacity Building')], default='select department', max_length=50)),
                ('directorate', models.CharField(blank=True, choices=[('', 'select directorate'), ('RQA', 'Research Quality Assurance'), ('IRB', 'Institutional Review Board'), ('KMC', 'Knowledge Management and Communications')], default='select directorate', max_length=50)),
                ('units', models.CharField(blank=True, choices=[('', 'select units'), ('IA', 'Internal Audit'), ('FM', 'Finance Management'), ('HRM', 'Human Resources Management'), ('PM', 'Procurement Management'), ('BA', 'Branch Administration'), ('ICT', 'ICT unit'), ('GC', 'Grants and Contracts'), ('TCB', 'Training and Capacity Building'), ('LAB', 'Laboratories'), ('DSP', 'Data Systems and Platforms'), ('CT', 'Clinical Trials'), ('CDCIM', 'Chronic Diseases Clinic in Ifakara and Mwananyamala')], default='select units', max_length=50)),
                ('position', models.CharField(max_length=50)),
                ('email', models.EmailField(default='', max_length=100)),
                ('background_and_education', models.TextField(default='')),
                ('professional_experience_and_skills', models.TextField(default='')),
                ('description', models.TextField(default='')),
                ('publication_link', models.URLField(blank=True)),
            ],
            options={
                'verbose_name_plural': 'Staffs Lists',
            },
        ),
    ]