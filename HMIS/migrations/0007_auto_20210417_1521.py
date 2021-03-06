# Generated by Django 3.2 on 2021-04-17 15:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('HMIS', '0006_auto_20210417_1442'),
    ]

    operations = [
        migrations.RenameField(
            model_name='registrationrecord',
            old_name='doctorID',
            new_name='doctor',
        ),
        migrations.RenameField(
            model_name='registrationrecord',
            old_name='patientID',
            new_name='patient',
        ),
        migrations.RenameField(
            model_name='treatmentrecord',
            old_name='doctorID',
            new_name='doctor',
        ),
        migrations.RenameField(
            model_name='treatmentrecord',
            old_name='patientID',
            new_name='patient',
        ),
    ]
