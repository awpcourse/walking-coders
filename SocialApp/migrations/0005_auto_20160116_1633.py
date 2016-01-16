# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('SocialApp', '0004_auto_20160116_1611'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='date_added',
            field=models.DateTimeField(default=datetime.datetime(2016, 1, 16, 16, 33, 5, 858000)),
        ),
        migrations.AlterField(
            model_name='post',
            name='date_added',
            field=models.DateTimeField(default=datetime.datetime(2016, 1, 16, 16, 33, 5, 858000)),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='avatar',
            field=models.ImageField(height_field=50, width_field=50, upload_to=b'images/'),
        ),
    ]
