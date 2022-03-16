# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0002_auto_20190327_1501'),
    ]

    operations = [
        migrations.AlterField(
            model_name='indexpromotionbanner',
            name='url',
            field=models.CharField(verbose_name='活动链接', max_length=256),
        ),
    ]
