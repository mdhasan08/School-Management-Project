# Generated by Django 4.0.1 on 2022-02-18 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0021_teacher_profile_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='birth_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
