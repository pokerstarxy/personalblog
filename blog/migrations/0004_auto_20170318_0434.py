# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-03-17 20:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20170317_0407'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num', models.CharField(max_length=20, unique=True)),
                ('date', models.TextField(blank=True, max_length=20)),
                ('name', models.TextField(max_length=100)),
                ('country', models.TextField(blank=True, max_length=20)),
                ('language', models.TextField(blank=True, max_length=50)),
                ('star', models.TextField(blank=True, max_length=200)),
                ('detail', models.TextField(blank=True, max_length=500)),
                ('xl_url', models.TextField(blank=True, max_length=150)),
                ('bd_url', models.TextField(blank=True, max_length=50)),
                ('bd_pwd', models.CharField(blank=True, max_length=5)),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['pub_date'],
                'verbose_name_plural': '\u7535\u5f71',
            },
        ),
        migrations.RemoveField(
            model_name='test',
            name='tag_test',
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='html_file',
            field=models.FileField(upload_to='x'),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='last_edit_date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='md_file',
            field=models.FileField(blank=True, upload_to='x'),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='blogpostimage',
            name='image',
            field=models.ImageField(upload_to='x'),
        ),
        migrations.DeleteModel(
            name='test',
        ),
    ]