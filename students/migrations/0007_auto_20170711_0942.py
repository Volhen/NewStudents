# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0006_auto_20170710_0951'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='group',
            options={'verbose_name': '\u0413\u0440\u0443\u043f\u043f\u0430', 'verbose_name_plural': '\u0413\u0440\u0443\u043f\u043f\u044b'},
        ),
        migrations.AlterModelOptions(
            name='student',
            options={'verbose_name': '\u0421\u0442\u0443\u0434\u0435\u043d\u0442', 'verbose_name_plural': '\u0421\u0442\u0443\u0434\u0435\u043d\u0442\u044b'},
        ),
        migrations.AlterField(
            model_name='group',
            name='notes',
            field=models.TextField(verbose_name='\u0414\u043e\u043f \u0437\u0430\u043c\u0435\u0442\u043a\u0438', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='group',
            name='title',
            field=models.CharField(max_length=256, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='student',
            name='birthday',
            field=models.DateField(null=True, verbose_name='\u0414\u0430\u0442\u0430 \u0440\u043e\u0436\u0434\u0435\u043d\u0438\u044f'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='student',
            name='first_name',
            field=models.CharField(max_length=256, verbose_name='\u0418\u043c\u044f'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='student',
            name='last_name',
            field=models.CharField(max_length=256, verbose_name='\u0424\u0430\u043c\u0438\u043b\u0438\u044f'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='student',
            name='middle_name',
            field=models.CharField(default=b'', max_length=256, verbose_name='\u041e\u0442\u0447\u0435\u0441\u0442\u0432\u043e', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='student',
            name='notes',
            field=models.TextField(verbose_name='\u0414\u043e\u043f \u0437\u0430\u043c\u0435\u0442\u043a\u0438', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='student',
            name='ticket',
            field=models.CharField(max_length=256, verbose_name='\u0411\u0438\u043b\u0435\u0442'),
            preserve_default=True,
        ),
    ]
