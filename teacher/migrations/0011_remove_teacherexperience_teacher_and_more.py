# Generated by Django 4.0.1 on 2022-02-08 05:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0010_teacherexperience_company_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacherexperience',
            name='teacher',
        ),
        migrations.DeleteModel(
            name='TeacherEducaionalQualification',
        ),
        migrations.DeleteModel(
            name='TeacherExperience',
        ),
    ]
