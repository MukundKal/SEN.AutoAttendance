# Generated by Django 3.0.3 on 2020-04-03 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prof_section', '0005_auto_20200404_0112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendancerecord',
            name='courseID',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='attendancerecord',
            name='studentID',
            field=models.CharField(max_length=10),
        ),
    ]