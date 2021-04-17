# Generated by Django 3.2 on 2021-04-14 22:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('HMIS', '0002_auto_20210411_1440'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('doctorID', models.CharField(max_length=8, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=15)),
                ('department', models.CharField(choices=[('ophthalmology', '眼科'), ('dentistry', '牙科')], max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('patientID', models.CharField(max_length=8, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='TreatmentRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('treTime', models.DateTimeField(auto_now_add=True)),
                ('doctorID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HMIS.doctor')),
                ('patientID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HMIS.patient')),
            ],
            options={
                'ordering': ['-treTime'],
            },
        ),
        migrations.CreateModel(
            name='TreatmentPlan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numAvailable', models.IntegerField(default=0)),
                ('doctorID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HMIS.doctor')),
            ],
        ),
        migrations.CreateModel(
            name='RegistrationRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('regTime', models.DateTimeField(auto_now_add=True)),
                ('isActive', models.BooleanField(default=True)),
                ('doctorID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HMIS.doctor')),
                ('patientID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HMIS.patient')),
            ],
            options={
                'ordering': ['-regTime'],
            },
        ),
    ]
