# Generated by Django 3.2.18 on 2023-07-27 18:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0004_auto_20230727_1808'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogpost',
            name='likes',
        ),
    ]