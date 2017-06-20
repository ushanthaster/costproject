# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('costapp', '0002_auto_20151126_1636'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='purchaseorder',
            name='payment',
        ),
        migrations.AddField(
            model_name='payment',
            name='purchase_order',
            field=models.ForeignKey(to='costapp.PurchaseOrder', default=''),
            preserve_default=False,
        ),
    ]
