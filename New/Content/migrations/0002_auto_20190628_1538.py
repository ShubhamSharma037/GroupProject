# Generated by Django 2.2.2 on 2019-06-28 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Content', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hmdesignimg',
            name='design_name',
            field=models.CharField(max_length=30),
        ),
    ]