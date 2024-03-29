# Generated by Django 2.2.5 on 2019-10-03 23:51

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('direct', '0009_auto_20190927_1033'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.DecimalField(decimal_places=2, max_digits=10)),
                ('paidTime', models.DateTimeField(default=datetime.datetime.now)),
                ('card', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='direct.Card')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='direct.Customer')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='direct.Product')),
            ],
        ),
    ]
