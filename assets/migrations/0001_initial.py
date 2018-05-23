# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-05-15 15:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AssetGroups',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True, verbose_name='\u8d44\u4ea7\u7ec4\u540d\u79f0')),
                ('desc', models.CharField(blank=True, max_length=100, null=True, verbose_name='\u63cf\u8ff0\u4fe1\u606f')),
            ],
            options={
                'db_table': 'assetgroups',
                'verbose_name': '\u8d44\u4ea7\u7ec4',
                'verbose_name_plural': '\u8d44\u4ea7\u7ec4',
                'permissions': (('can_add_assetgroup', '\u6dfb\u52a0\u8d44\u4ea7\u7ec4'), ('can_change_assetgroup', '\u4fee\u6539\u8d44\u4ea7\u7ec4'), ('can_delete_assetgroup', '\u5220\u9664\u8d44\u4ea7\u7ec4'), ('can_view_assetgroup', '\u67e5\u770b\u8d44\u4ea7\u7ec4')),
            },
        ),
        migrations.CreateModel(
            name='Assets',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('update_time', models.DateTimeField(auto_created=True, auto_now=True, verbose_name='\u66f4\u65b0\u65f6\u95f4')),
                ('hostname', models.CharField(max_length=50, unique=True, verbose_name='\u4e3b\u673a\u540d')),
                ('ip', models.GenericIPAddressField(verbose_name='\u7ba1\u7406IP')),
                ('other_ip', models.CharField(blank=True, max_length=100, null=True, verbose_name='\u5176\u5b83IP')),
                ('asset_type', models.CharField(blank=True, choices=[(b'1', '\u7269\u7406\u673a'), (b'2', '\u865a\u62df\u673a'), (b'3', '\u5bb9\u5668'), (b'4', '\u7f51\u7edc\u8bbe\u5907'), (b'5', '\u5176\u4ed6')], max_length=30, null=True, verbose_name='\u8bbe\u5907\u7c7b\u578b')),
                ('status', models.CharField(blank=True, choices=[(b'1', '\u4f7f\u7528\u4e2d'), (b'2', '\u672a\u4f7f\u7528'), (b'3', '\u6545\u969c'), (b'4', '\u5176\u5b83')], max_length=30, null=True, verbose_name='\u8bbe\u5907\u72b6\u6001')),
                ('os', models.CharField(blank=True, max_length=100, null=True, verbose_name='\u64cd\u4f5c\u7cfb\u7edf')),
                ('cpu_num', models.CharField(blank=True, max_length=100, null=True, verbose_name='CPU\u6570\u91cf')),
                ('memory', models.CharField(blank=True, max_length=30, null=True, verbose_name='\u5185\u5b58\u5927\u5c0f')),
                ('disk', models.CharField(blank=True, max_length=255, null=True, verbose_name='\u786c\u76d8\u4fe1\u606f')),
                ('sn', models.CharField(blank=True, max_length=60, verbose_name='SN\u53f7\u7801')),
                ('usage', models.CharField(blank=True, max_length=100, null=True, verbose_name='\u7528\u9014')),
                ('application', models.CharField(blank=True, max_length=100, null=True, verbose_name='\u8f6f\u4ef6')),
                ('principal', models.CharField(blank=True, max_length=50, null=True, verbose_name='\u8d1f\u8d23\u4eba')),
                ('memo', models.TextField(blank=True, max_length=200, null=True, verbose_name='\u5907\u6ce8\u4fe1\u606f')),
                ('jira', models.CharField(blank=True, max_length=200, null=True, verbose_name='\u7533\u8bf7jira')),
                ('add_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='\u6dfb\u52a0\u65f6\u95f4')),
                ('group', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='assets.AssetGroups', verbose_name='\u8d44\u4ea7\u7ec4')),
            ],
            options={
                'db_table': 'assets',
                'verbose_name': '\u8d44\u4ea7\u4fe1\u606f',
                'verbose_name_plural': '\u8d44\u4ea7\u4fe1\u606f',
                'permissions': (('can_add_asset', '\u6dfb\u52a0\u8d44\u4ea7'), ('can_change_asset', '\u4fee\u6539\u8d44\u4ea7'), ('can_delete_asset', '\u5220\u9664\u8d44\u4ea7'), ('can_view_asset', '\u67e5\u770b\u8d44\u4ea7')),
            },
        ),
        migrations.CreateModel(
            name='Idc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, null=True, verbose_name='\u673a\u623f\u540d\u79f0')),
                ('address', models.CharField(max_length=100, null=True, verbose_name='\u673a\u623f\u5730\u5740')),
                ('tel', models.CharField(max_length=30, null=True, verbose_name='\u673a\u623f\u7535\u8bdd')),
                ('contact', models.CharField(max_length=30, null=True, verbose_name='\u5ba2\u6237\u7ecf\u7406')),
            ],
            options={
                'db_table': 'idc',
                'verbose_name': '\u673a\u623f',
                'verbose_name_plural': '\u673a\u623f',
                'permissions': (('can_add_idc', '\u6dfb\u52a0\u673a\u623f'), ('can_change_idc', '\u4fee\u6539\u673a\u623f'), ('can_delete_idc', '\u5220\u9664\u673a\u623f'), ('can_view_idc', '\u67e5\u770b\u673a\u623f')),
            },
        ),
        migrations.AddField(
            model_name='assets',
            name='idc',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='assets.Idc', verbose_name='\u6240\u5728\u673a\u623f'),
        ),
    ]
