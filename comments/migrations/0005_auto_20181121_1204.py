# Generated by Django 2.1.3 on 2018-11-21 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0004_auto_20181120_1723'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='parentId',
            field=models.ForeignKey(null=True, on_delete=None, related_name='replies', to='comments.Comment'),
        ),
    ]
