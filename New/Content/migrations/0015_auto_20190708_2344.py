# Generated by Django 2.2.2 on 2019-07-08 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Content', '0014_auto_20190708_2341'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cstmrfeed',
            name='cst_feed_msg',
            field=models.CharField(max_length=1000, verbose_name='Feedback Message'),
        ),
    ]