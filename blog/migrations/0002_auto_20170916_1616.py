# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='created_dae',
            new_name='created_date',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='pblished_date',
            new_name='published_date',
        ),
    ]
