# Generated by Django 2.1.2 on 2019-09-22 13:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realtors', '0020_auto_20190915_2137'),
    ]

    operations = [
        migrations.AlterField(
            model_name='realtor',
            name='hire_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 9, 22, 15, 47, 43, 577281)),
        ),
    ]
