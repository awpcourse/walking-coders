# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('SocialApp', '0003_auto_20160116_1549'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='date_added',
            field=models.DateTimeField(default=datetime.datetime(2016, 1, 16, 16, 11, 7, 294000)),
        ),
        migrations.AlterField(
            model_name='post',
            name='date_added',
            field=models.DateTimeField(default=datetime.datetime(2016, 1, 16, 16, 11, 7, 294000)),
        ),
    ]
