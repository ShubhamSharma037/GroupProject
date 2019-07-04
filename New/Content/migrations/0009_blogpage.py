# Generated by Django 2.2.2 on 2019-07-03 04:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Content', '0008_clientsnlinks'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blg_topic', models.CharField(max_length=50)),
                ('blg_desc', models.CharField(max_length=10000)),
                ('blg_link', models.CharField(max_length=400)),
                ('blg_date', models.DateField(default=datetime.date.today)),
                ('blg_name_blgger', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name': 'BlogUpdate',
                'verbose_name_plural': 'BlogUpdates',
            },
        ),
    ]
