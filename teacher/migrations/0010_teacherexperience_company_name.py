# Generated by Django 4.0 on 2022-02-07 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0009_alter_teachereducaionalqualification_honours_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacherexperience',
            name='company_name',
            field=models.CharField(default='', max_length=20),
        ),
    ]
