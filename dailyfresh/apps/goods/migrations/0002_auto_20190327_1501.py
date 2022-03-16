# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goods',
            name='create_time',
            field=models.DateTimeField(verbose_name='创建时间', auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='goods',
            name='update_time',
            field=models.DateTimeField(verbose_name='更新时间', auto_now=True),
        ),
        migrations.AlterField(
            model_name='goodsimage',
            name='create_time',
            field=models.DateTimeField(verbose_name='创建时间', auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='goodsimage',
            name='update_time',
            field=models.DateTimeField(verbose_name='更新时间', auto_now=True),
        ),
        migrations.AlterField(
            model_name='goodssku',
            name='create_time',
            field=models.DateTimeField(verbose_name='创建时间', auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='goodssku',
            name='update_time',
            field=models.DateTimeField(verbose_name='更新时间', auto_now=True),
        ),
        migrations.AlterField(
            model_name='goodstype',
            name='create_time',
            field=models.DateTimeField(verbose_name='创建时间', auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='goodstype',
            name='update_time',
            field=models.DateTimeField(verbose_name='更新时间', auto_now=True),
        ),
        migrations.AlterField(
            model_name='indexgoodsbanner',
            name='create_time',
            field=models.DateTimeField(verbose_name='创建时间', auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='indexgoodsbanner',
            name='update_time',
            field=models.DateTimeField(verbose_name='更新时间', auto_now=True),
        ),
        migrations.AlterField(
            model_name='indexpromotionbanner',
            name='create_time',
            field=models.DateTimeField(verbose_name='创建时间', auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='indexpromotionbanner',
            name='update_time',
            field=models.DateTimeField(verbose_name='更新时间', auto_now=True),
        ),
        migrations.AlterField(
            model_name='indextypegoodsbanner',
            name='create_time',
            field=models.DateTimeField(verbose_name='创建时间', auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='indextypegoodsbanner',
            name='update_time',
            field=models.DateTimeField(verbose_name='更新时间', auto_now=True),
        ),
    ]


