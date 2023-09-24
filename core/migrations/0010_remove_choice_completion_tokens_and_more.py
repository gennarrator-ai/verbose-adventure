# Generated by Django 4.2.5 on 2023-09-23 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_rename_chatcmpl_from_summary_chatcmpl_responded_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='choice',
            name='completion_tokens',
        ),
        migrations.RemoveField(
            model_name='choice',
            name='prompt_tokens',
        ),
        migrations.AddField(
            model_name='chatcmpl',
            name='completion_tokens',
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='chatcmpl',
            name='prompt_tokens',
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
    ]
