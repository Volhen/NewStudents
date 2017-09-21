# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0003_auto_20170918_1023'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exam',
            name='groups_name',
            field=models.CharField(default=1, max_length=256, verbose_name='\u0413\u0440\u0443\u043f\u043f\u0430 \u043d\u0430 \u044d\u043a\u0437\u0430\u043c\u0435\u043d\u0435'),
            preserve_default=False,
        ),
    ]
