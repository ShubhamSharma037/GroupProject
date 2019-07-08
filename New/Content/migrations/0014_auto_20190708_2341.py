# Generated by Django 2.2.2 on 2019-07-08 18:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Content', '0013_merge_20190704_1814'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cstmrfeed',
            name='cst_img',
        ),
        migrations.RemoveField(
            model_name='cstmrfeed',
            name='wrk_at_as',
        ),
        migrations.AlterField(
            model_name='blogpage',
            name='blg_date',
            field=models.DateField(default=datetime.date.today, verbose_name='Blog Date'),
        ),
        migrations.AlterField(
            model_name='blogpage',
            name='blg_desc',
            field=models.TextField(max_length=10000, verbose_name='Blog Content'),
        ),
        migrations.AlterField(
            model_name='blogpage',
            name='blg_name_blgger',
            field=models.CharField(max_length=20, verbose_name='Blogger Name'),
        ),
        migrations.AlterField(
            model_name='blogpage',
            name='blg_pic',
            field=models.CharField(max_length=2000, verbose_name='Blog Image'),
        ),
        migrations.AlterField(
            model_name='blogpage',
            name='blg_topic',
            field=models.CharField(max_length=50, verbose_name='Blog Name'),
        ),
    ]
