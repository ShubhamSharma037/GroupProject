# Generated by Django 2.2.2 on 2019-06-30 08:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Content', '0006_teammembers'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cstmrfeed',
            options={'verbose_name': 'Customer Feedback', 'verbose_name_plural': 'Customer Feedback'},
        ),
        migrations.AlterModelOptions(
            name='hmdesignimg',
            options={'verbose_name': 'Home Design Image', 'verbose_name_plural': 'Home Design images'},
        ),
        migrations.AlterModelOptions(
            name='teammembers',
            options={'verbose_name': 'Team Member', 'verbose_name_plural': 'Team Members'},
        ),
    ]
