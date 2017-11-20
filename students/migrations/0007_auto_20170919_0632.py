# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0006_auto_20170919_0630'),
    ]

    operations = [
        migrations.RenameField(
            model_name='exam',
            old_name='name',
            new_name='groups_name',
        ),
    ]
