# Generated by Django 4.0 on 2021-12-20 11:26

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('base', '0003_remove_todoer_user_todoer_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='economy',
            name='user',
        ),
        migrations.AddField(
            model_name='economy',
            name='user',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
