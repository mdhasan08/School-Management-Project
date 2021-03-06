# Generated by Django 4.0.1 on 2022-01-31 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('surname', models.CharField(max_length=20)),
                ('father_name', models.CharField(max_length=20)),
                ('mother_name', models.CharField(max_length=20)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=10)),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('religion', models.CharField(choices=[('Muslim', 'Muslim'), ('Hindu', 'Hindu'), ('Cristian', 'Cristian'), ('Buddist', 'Buddist')], max_length=10)),
                ('email', models.EmailField(max_length=100)),
                ('phone', models.CharField(max_length=14)),
                ('address', models.TextField(max_length=100)),
                ('blood_group', models.TextField(max_length=3)),
            ],
        ),
    ]
