# Generated by Django 2.1.15 on 2020-11-18 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ihi_wepapp', '0008_auto_20200404_1430'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staffs',
            name='units',
            field=models.CharField(blank=True, choices=[('', 'select units'), ('IA', 'Internal Audit'), ('FM', 'Finance Management'), ('HRM', 'Human Resources Management'), ('PM', 'Procurement Management'), ('BA', 'Branch Administration'), ('ICT', 'ICT unit'), ('GC', 'Grants and Contracts'), ('TCB', 'Training and Capacity Building'), ('LAB', 'Laboratories'), ('DSP', 'Data Systems and Platforms'), ('CT', 'Clinical Trials'), ('CDCIM', 'Chronic Diseases Clinic in Ifakara and Mwananyamala'), ('TRANSPORT', 'Transport'), ('IH', 'Ifakara Hub')], default='select units', max_length=50),
        ),
    ]
