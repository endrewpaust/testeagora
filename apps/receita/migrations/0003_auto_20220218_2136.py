# Generated by Django 2.2.6 on 2022-02-19 00:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('receita', '0002_auto_20220218_1835'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receita_modelo',
            name='data_receita',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 2, 18, 21, 36, 45, 692920)),
        ),
    ]
