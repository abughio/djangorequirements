# Generated by Django 2.1.3 on 2018-12-24 09:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('requirements', '0002_auto_20181223_1249'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usecase',
            old_name='extendes',
            new_name='extends',
        ),
    ]
