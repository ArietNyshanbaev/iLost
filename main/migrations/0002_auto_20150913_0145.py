# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cardstick',
            options={'verbose_name': '\u041a\u0430\u0440\u0442\u0430', 'verbose_name_plural': '\u041a\u0430\u0440\u0442\u044b'},
        ),
        migrations.AlterField(
            model_name='cardstick',
            name='card_id',
            field=models.CharField(unique=True, max_length=7),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='cardstick',
            name='email',
            field=models.CharField(default=b'', max_length=50, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='cardstick',
            name='name',
            field=models.CharField(default=b'', max_length=100, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='cardstick',
            name='telephone',
            field=models.CharField(default=b'', max_length=20, null=True, blank=True),
            preserve_default=True,
        ),
    ]
