# Generated by Django 2.1.3 on 2018-11-13 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0002_auto_20181113_1718'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='title',
            field=models.CharField(max_length=300),
        ),
    ]