# Generated by Django 2.0.4 on 2018-06-26 00:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HospitalActivity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('image', models.CharField(max_length=200)),
                ('location', models.CharField(max_length=200)),
                ('volunteers', models.IntegerField()),
                ('novice', models.IntegerField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('duration', models.IntegerField()),
                ('schedule', models.DateTimeField()),
                ('novice_list', models.CharField(blank=True, default='', max_length=10000)),
                ('selected', models.CharField(blank=True, default='', max_length=10000)),
                ('waiting', models.CharField(blank=True, default='', max_length=10000)),
            ],
        ),
        migrations.CreateModel(
            name='NGOActivity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('image', models.CharField(max_length=200)),
                ('location', models.CharField(max_length=200)),
                ('volunteers', models.IntegerField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('duration', models.IntegerField()),
                ('schedule', models.DateTimeField()),
                ('selected', models.CharField(default='', max_length=10000)),
                ('waiting', models.CharField(default='', max_length=10000)),
            ],
        ),
    ]
