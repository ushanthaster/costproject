# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('costapp', '0003_auto_20151128_1839'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='budget',
            name='change',
        ),
        migrations.AddField(
            model_name='budgetchange',
            name='budget',
            field=models.ForeignKey(to='costapp.Budget', default=''),
            preserve_default=False,
        ),
    ]
