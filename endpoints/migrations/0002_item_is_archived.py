# Generated by Django 3.0.8 on 2021-05-07 04:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('endpoints', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='is_archived',
            field=models.BooleanField(default=False),
        ),
    ]
