# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0005_auto_20170918_1219'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exam',
            name='groups_name',
        ),
        migrations.AddField(
            model_name='exam',
            name='name',
            field=models.CharField(default=1, max_length=256, verbose_name='\u0424\u0418\u041e '),
            preserve_default=False,
        ),
    ]
