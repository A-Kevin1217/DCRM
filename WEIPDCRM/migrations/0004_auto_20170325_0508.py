# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-25 04:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('WEIPDCRM', '0003_auto_20170310_1609'),
    ]

    operations = [
        migrations.AddField(
            model_name='release',
            name='email',
            field=models.EmailField(blank=True, help_text="Maintainer's E-Mail to provide support.", max_length=255, null=True, verbose_name='E-Mail'),
        ),
        migrations.AlterField(
            model_name='setting',
            name='active_release',
            field=models.ForeignKey(blank=True, default=None, help_text='Each repository should have an active release, otherwise it will not be recognized by any advanced package tools.', null=True, on_delete=django.db.models.deletion.SET_NULL, to='WEIPDCRM.Release', verbose_name='Active Release'),
        ),
        migrations.AlterField(
            model_name='setting',
            name='duoshuo_comments',
            field=models.BooleanField(default=False, help_text='Enable DuoShuo comments', verbose_name='DuoShuo Comments'),
        ),
        migrations.AlterField(
            model_name='setting',
            name='duoshuo_shortname',
            field=models.CharField(blank=True, default='', help_text='Please visit <a href="http://duoshuo.com/">http://duoshuo.com</a> and register to use Duoshuo.', max_length=255, verbose_name='DuoShuo Short Name'),
        ),
    ]
