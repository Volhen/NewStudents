# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0007_auto_20170919_0632'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exam',
            name='groups_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, verbose_name='\u0413\u0440\u0443\u043f\u043f\u0430', to='students.Group', null=True),
            preserve_default=True,
        ),
    ]
