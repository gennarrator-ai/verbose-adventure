# Generated by Django 4.2.5 on 2023-09-22 02:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='iteration',
            field=models.PositiveIntegerField(default=0),
        ),
    ]