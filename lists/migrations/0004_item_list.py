# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0003_auto_20151008_2249'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='list',
            field=models.ForeignKey(default=None, to='lists.List'),
        ),
    ]
