# Generated by Django 4.0.1 on 2022-02-08 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0015_teacherexperience_teachereducaionalqualification'),
    ]

    operations = [
        migrations.RenameField(
            model_name='teacherexperience',
            old_name='company_name',
            new_name='institute_name',
        ),
        migrations.AlterField(
            model_name='teachereducaionalqualification',
            name='grade_point',
            field=models.FloatField(),
        ),
    ]
