# Generated by Django 4.0.1 on 2022-01-31 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='nationality',
            field=models.CharField(default='Bangladeshi', max_length=15),
        ),
    ]
