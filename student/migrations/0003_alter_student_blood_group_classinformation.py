# Generated by Django 4.0 on 2022-02-01 04:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_student_nationality'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='blood_group',
            field=models.CharField(choices=[('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), ('B-', 'B-'), ('AB+', 'AB+'), ('AB-', 'AB-'), ('O+', '0+'), ('O-', '0-')], max_length=3),
        ),
        migrations.CreateModel(
            name='ClassInformation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_class', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')], max_length=3)),
                ('class_roll', models.PositiveIntegerField()),
                ('section', models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')], default='A', max_length=1)),
                ('admission_date', models.DateField()),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='student.student')),
            ],
        ),
    ]
