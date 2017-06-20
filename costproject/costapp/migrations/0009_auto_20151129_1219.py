# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('costapp', '0008_invoice_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='budgetchange',
            name='approved',
        ),
        migrations.RemoveField(
            model_name='budgetchange',
            name='rejected',
        ),
        migrations.AddField(
            model_name='budgetchange',
            name='status',
            field=models.IntegerField(choices=[(0, 'pending'), (1, 'rejected'), (2, 'approved')], default=0),
        ),
    ]
