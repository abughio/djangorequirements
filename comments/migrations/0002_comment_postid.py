# Generated by Django 2.1.3 on 2018-11-20 13:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_summary'),
        ('comments', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='postId',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='blog.Post'),
        ),
    ]
