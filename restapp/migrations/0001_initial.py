# Generated by Django 4.1.7 on 2023-03-01 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_name', models.CharField(max_length=250)),
                ('task_des', models.CharField(max_length=250)),
                ('date_created', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]