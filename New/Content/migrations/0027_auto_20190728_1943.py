# Generated by Django 2.2.3 on 2019-07-28 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Content', '0026_auto_20190717_0216'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prjimg',
            name='design_img_link',
            field=models.ImageField(blank=True, upload_to='admin_photo', verbose_name='Image Link'),
        ),
    ]
