# Generated by Django 2.1.3 on 2018-12-07 18:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
        ),
        migrations.CreateModel(
            name='Cat',
            fields=[
                ('animal_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='projects.Animal')),
                ('family', models.CharField(max_length=200)),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('projects.animal',),
        ),
        migrations.CreateModel(
            name='Dog',
            fields=[
                ('animal_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='projects.Animal')),
                ('breed', models.CharField(max_length=200)),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('projects.animal',),
        ),
        migrations.AddField(
            model_name='animal',
            name='polymorphic_ctype',
            field=models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='polymorphic_projects.animal_set+', to='contenttypes.ContentType'),
        ),
    ]
