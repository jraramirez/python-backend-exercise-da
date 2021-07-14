# Generated by Django 3.2.2 on 2021-07-14 01:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('endpoints', '0003_auto_20210714_0122'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=50)),
                ('manufacturer', models.CharField(max_length=50)),
            ],
        ),
    ]