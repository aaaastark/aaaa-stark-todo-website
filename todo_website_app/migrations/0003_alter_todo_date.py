# Generated by Django 3.2 on 2021-04-25 22:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_website_app', '0002_auto_20210423_2258'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='date',
            field=models.DateField(),
        ),
    ]