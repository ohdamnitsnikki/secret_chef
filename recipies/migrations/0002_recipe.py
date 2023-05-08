# Generated by Django 3.2.18 on 2023-05-07 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipies', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('category', models.CharField(max_length=20)),
                ('photo', models.ImageField(upload_to='recipes')),
            ],
        ),
    ]