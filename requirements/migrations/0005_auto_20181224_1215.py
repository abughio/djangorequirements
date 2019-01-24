# Generated by Django 2.1.3 on 2018-12-24 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('requirements', '0004_auto_20181224_1214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usecase',
            name='extends',
            field=models.ForeignKey(blank=True, null=True, on_delete=None, related_name='included_by', to='requirements.Usecase'),
        ),
        migrations.AlterField(
            model_name='usecase',
            name='includes',
            field=models.ForeignKey(blank=True, null=True, on_delete=None, related_name='extended_by', to='requirements.Usecase'),
        ),
    ]
