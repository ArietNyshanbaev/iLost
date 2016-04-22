# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cardstick',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('card_id', models.CharField(max_length=7)),
                ('activated', models.BooleanField(default=False)),
                ('telephone', models.CharField(default=b'', max_length=20)),
                ('email', models.CharField(default=b'', max_length=50)),
                ('name', models.CharField(default=b'', max_length=100)),
            ],
            options={
                'verbose_name': '\u043a\u0430rta',
                'verbose_name_plural': '\u043a\u0430rty',
            },
            bases=(models.Model,),
        ),
    ]
