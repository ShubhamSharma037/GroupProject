# Generated by Django 2.2.2 on 2019-06-28 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Content', '0004_cstmrfeed'),
    ]

    operations = [
        migrations.AddField(
            model_name='cstmrfeed',
            name='cst_img',
            field=models.CharField(default=0, max_length=2000),
            preserve_default=False,
        ),
    ]