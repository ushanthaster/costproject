# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('costapp', '0005_auto_20151129_0958'),
    ]

    operations = [
        migrations.RenameField(
            model_name='budgetchange',
            old_name='committed_amount',
            new_name='value_of_change',
        ),
    ]
