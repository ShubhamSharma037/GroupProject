# Generated by Django 2.2.3 on 2019-08-16 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Content', '0030_remove_prjimg_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hmdesignimg',
            name='design_img_link',
            field=models.ImageField(max_length=2000, upload_to='', verbose_name='Image Link'),
        ),
    ]