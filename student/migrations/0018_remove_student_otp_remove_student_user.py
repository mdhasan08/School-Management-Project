# Generated by Django 4.0.1 on 2022-02-20 11:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0017_student_user'),
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
