# Generated by Django 3.2 on 2021-04-16 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HMIS', '0003_doctor_patient_registrationrecord_treatmentplan_treatmentrecord'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='password',
            field=models.CharField(default='123', max_length=256),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='patient',
            name='password',
            field=models.CharField(default='123', max_length=256),
            preserve_default=False,
        ),
    ]
