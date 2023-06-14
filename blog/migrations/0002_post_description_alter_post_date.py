# Generated by Django 4.2.1 on 2023-06-04 19:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='description',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateField(default=datetime.date.today),
        ),
    ]