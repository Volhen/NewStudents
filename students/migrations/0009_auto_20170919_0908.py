# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0008_auto_20170919_0852'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exam',
            name='date_time',
            field=models.DateTimeField(null=True, verbose_name='\u0414\u0430\u0442\u0430 \u0438 \u0432\u0440\u0435\u043c\u044f \u043f\u0440\u043e\u0432\u0435\u0434\u0435\u043d\u0438\u044f \u044d\u043a\u0437\u0430\u043c\u0435\u043d\u0430'),
            preserve_default=True,
        ),
    ]
