# Generated by Django 4.0 on 2021-12-20 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_remove_economy_id_remove_todoer_id_economy_e_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='economy',
            name='Date',
            field=models.DateField(default=None),
            preserve_default=False,
        ),
    ]
