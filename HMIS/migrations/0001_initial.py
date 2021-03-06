# Generated by Django 3.2 on 2021-04-10 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_id', models.CharField(max_length=8, unique=True)),
                ('name', models.CharField(max_length=10)),
                ('password', models.CharField(max_length=256)),
                ('gender', models.CharField(choices=[('male', '男'), ('female', '女')], max_length=32)),
                ('age', models.IntegerField()),
                ('department', models.CharField(max_length=32)),
                ('c_time', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': '用户',
                'verbose_name_plural': '用户',
                'ordering': ['-c_time'],
            },
        ),
    ]
