# Generated by Django 2.2.3 on 2019-07-28 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Content', '0027_auto_20190728_1943'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prjimg',
            name='design_img_link',
            field=models.FileField(blank=True, upload_to='post_image', verbose_name='Image Link'),
        ),
    ]
