# Generated by Django 4.0.1 on 2022-02-10 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0012_student_archived_at_student_archived_by_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='classinformation',
            name='archived_at',
            field=models.DateTimeField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='classinformation',
            name='archived_by',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='classinformation',
            name='archived_from',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='classinformation',
            name='created_by',
            field=models.DateTimeField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='classinformation',
            name='created_from',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='classinformation',
            name='is_archived',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='classinformation',
            name='modified_at',
            field=models.DateTimeField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='classinformation',
            name='modified_by',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='classinformation',
            name='modified_from',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='subject',
            name='archived_at',
            field=models.DateTimeField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='subject',
            name='archived_by',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='subject',
            name='archived_from',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='subject',
            name='created_by',
            field=models.DateTimeField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='subject',
            name='created_from',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='subject',
            name='is_archived',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='subject',
            name='modified_at',
            field=models.DateTimeField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='subject',
            name='modified_by',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='subject',
            name='modified_from',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
