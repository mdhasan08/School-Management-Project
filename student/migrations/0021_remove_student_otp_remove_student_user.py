# Generated by Django 4.0.1 on 2022-02-21 15:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0020_student_otp_student_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='otp',
        ),
        migrations.RemoveField(
            model_name='student',
            name='user',
        ),
    ]
