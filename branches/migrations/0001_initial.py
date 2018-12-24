# Generated by Django 2.1.3 on 2018-12-09 10:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('retailerMainName', models.CharField(max_length=255)),
                ('retailerNameEN', models.CharField(max_length=200)),
                ('retailerNameAR', models.CharField(max_length=200)),
                ('iban', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('nameAR', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('nameAR', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='city',
            name='region',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cities', to='branches.Region'),
        ),
        migrations.AddField(
            model_name='branch',
            name='city',
            field=models.ForeignKey(on_delete=None, related_name='branches', to='branches.City'),
        ),
        migrations.AddField(
            model_name='branch',
            name='region',
            field=models.ForeignKey(on_delete=None, related_name='branches', to='branches.Region'),
        ),
    ]