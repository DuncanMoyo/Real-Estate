# Generated by Django 2.1.2 on 2019-09-09 17:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realtors', '0005_auto_20190909_1312'),
    ]

    operations = [
        migrations.AlterField(
            model_name='realtor',
            name='hire_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 9, 9, 19, 52, 27, 101049)),
        ),
    ]
