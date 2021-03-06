# Generated by Django 4.0.1 on 2022-02-08 05:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0011_remove_teacherexperience_teacher_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='TeacherExperience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(default='', max_length=20)),
                ('job_name', models.CharField(max_length=20)),
                ('job_designation', models.CharField(max_length=10)),
                ('joining_year', models.PositiveIntegerField()),
                ('job_duration', models.CharField(max_length=8)),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='Teacher_Experience', to='teacher.teacher')),
            ],
        ),
        migrations.CreateModel(
            name='TeacherEducaionalQualification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('degree', models.CharField(choices=[('Honours', 'Honours'), ('BSC', 'BSC'), ('BBA', 'BBA'), ('MSC', 'MSC'), ('MBA', 'MBA'), ('PhD', 'PhD')], max_length=7)),
                ('passing_year', models.PositiveIntegerField()),
                ('board', models.CharField(max_length=8)),
                ('grade_point', models.PositiveIntegerField()),
                ('point_out_of', models.PositiveIntegerField(choices=[('5.00', '5.00'), ('4.00', '4.00')])),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='Teacher_Educaional_Qualification', to='teacher.teacher')),
            ],
        ),
    ]
