# Generated by Django 2.2.5 on 2019-09-18 09:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('direct', '0005_auto_20190918_1908'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='firstName',
            new_name='first_Name',
        ),
        migrations.RenameField(
            model_name='customer',
            old_name='lastName',
            new_name='last_Name',
        ),
    ]
