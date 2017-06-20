# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('costapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Budget',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('amount', models.DecimalField(max_digits=20, decimal_places=2)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='BudgetCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='BudgetChange',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('committed_amount', models.DecimalField(max_digits=20, decimal_places=2)),
                ('reason_for_change', models.CharField(max_length=200)),
                ('date', models.DateTimeField(verbose_name='date')),
                ('rejected', models.BooleanField()),
                ('approved', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('amount', models.DecimalField(max_digits=20, decimal_places=2)),
            ],
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('contact_point', models.CharField(max_length=200)),
                ('contact_phone', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='budget',
            name='category',
            field=models.ForeignKey(to='costapp.BudgetCategory'),
        ),
        migrations.AddField(
            model_name='budget',
            name='change',
            field=models.ForeignKey(to='costapp.BudgetChange'),
        ),
        migrations.AddField(
            model_name='purchaseorder',
            name='budget',
            field=models.ForeignKey(default='', to='costapp.Budget'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='purchaseorder',
            name='invoice',
            field=models.ForeignKey(default='', to='costapp.Invoice'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='purchaseorder',
            name='supplier',
            field=models.ForeignKey(default='', to='costapp.Supplier'),
            preserve_default=False,
        ),
    ]
