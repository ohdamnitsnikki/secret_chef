# Generated by Django 3.2.18 on 2023-07-27 18:08

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('post', '0003_alter_blogpost_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blogpost',
            options={'ordering': ['-created_on'], 'verbose_name': 'User Post', 'verbose_name_plural': 'User Posts'},
        ),
        migrations.AddField(
            model_name='blogpost',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='blogpost_like', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='blogpost',
            name='status',
            field=models.IntegerField(choices=[(0, 'Draft'), (1, 'Published')], default=0),
        ),
    ]
