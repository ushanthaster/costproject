# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('costapp', '0004_auto_20151129_0952'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='purchaseorder',
            name='invoice',
        ),
        migrations.AddField(
            model_name='invoice',
            name='purchase_order',
            field=models.ForeignKey(to='costapp.PurchaseOrder', default=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='budgetchange',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
