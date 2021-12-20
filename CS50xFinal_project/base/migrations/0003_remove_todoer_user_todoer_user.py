# Generated by Django 4.0 on 2021-12-20 11:25

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('base', '0002_delete_passwordresetcodes_delete_token'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todoer',
            name='user',
        ),
        migrations.AddField(
            model_name='todoer',
            name='user',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
