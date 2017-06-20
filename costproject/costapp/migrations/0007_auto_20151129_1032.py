# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('costapp', '0006_auto_20151129_1028'),
    ]

    operations = [
        migrations.RenameField(
            model_name='budget',
            old_name='amount',
            new_name='original_budget_amount',
        ),
    ]
