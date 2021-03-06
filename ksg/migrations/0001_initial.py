# Generated by Django 3.2.12 on 2022-03-30 07:26

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='dj_ksg_p',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('name', models.TextField()),
                ('c_prof', models.IntegerField()),
                ('smj_prof', django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(blank=True, null=True), blank=True, null=True, size=None)),
                ('KSG', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'ksg_p',
                'ordering': ['id'],
            },
        ),
    ]
