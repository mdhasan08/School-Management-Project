# Generated by Django 4.0.1 on 2022-02-20 04:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0027_alter_teacher_birth_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='salary',
            field=models.PositiveIntegerField(blank=True, max_length=10, null=True),
        ),
    ]
