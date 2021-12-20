# Generated by Django 4.0 on 2021-12-20 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_remove_economy_user_economy_user_remove_todoer_user_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='economy',
            name='id',
        ),
        migrations.RemoveField(
            model_name='todoer',
            name='id',
        ),
        migrations.AddField(
            model_name='economy',
            name='E_ID',
            field=models.AutoField(default=None, primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='todoer',
            name='T_ID',
            field=models.AutoField(default=None, primary_key=True, serialize=False),
            preserve_default=False,
        ),
    ]
