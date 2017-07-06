# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_auto_20170703_0839'),
    ]

    operations = [
        migrations.RenameField(
            model_name='group',
            old_name='loader',
            new_name='leader',
        ),
    ]
