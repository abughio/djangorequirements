# Generated by Django 2.1.3 on 2018-12-07 06:33

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField(default=' - ', max_length=500)),
                ('client_name', models.CharField(max_length=200)),
                ('expected_start', models.DateTimeField(default=django.utils.timezone.now)),
                ('expected_finish', models.DateTimeField(default=django.utils.timezone.now)),
                ('category', models.ForeignKey(on_delete=None, to='projects.Category')),
            ],
        ),
    ]