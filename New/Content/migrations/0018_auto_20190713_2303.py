# Generated by Django 2.2.3 on 2019-07-13 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Content', '0017_auto_20190712_2330'),
    ]

    operations = [
        migrations.CreateModel(
            name='PrjImg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('design_name', models.CharField(max_length=30, verbose_name='Design Name')),
                ('design_type', models.CharField(max_length=20, verbose_name='Design Type(Interior/Exterior)')),
                ('design_img_link', models.CharField(max_length=2000, verbose_name='Image Link')),
            ],
            options={
                'verbose_name': 'Project Page Designs Image',
                'verbose_name_plural': 'Project Page Design Images',
            },
        ),
        migrations.DeleteModel(
            name='ClientsNLinks',
        ),
        migrations.DeleteModel(
            name='TeamMembers',
        ),
    ]
