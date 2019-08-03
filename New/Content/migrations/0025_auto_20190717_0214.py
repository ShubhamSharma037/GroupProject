# Generated by Django 2.2.3 on 2019-07-16 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Content', '0024_auto_20190717_0205'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prjimg',
            name='design_type',
            field=models.CharField(choices=[('Bed Room', 'Bed Room'), ('Drawing Room', 'Drawing Room'), ('Kids Room', 'Kids Room'), ('Ceiling', 'Ceiling'), ('Wardrobe', 'Wardrobe'), ('Kitchen', 'Kitchen'), ('Living Room', 'Living Room'), ('Dinning Room', 'Dinning Room')], max_length=30, verbose_name='Design Type'),
        ),
    ]