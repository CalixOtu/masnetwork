# Generated by Django 3.2.7 on 2024-01-01 16:46

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0012_auto_20231231_1753'),
    ]

    operations = [
        migrations.AddField(
            model_name='worldcup',
            name='mails',
            field=models.JSONField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='pins',
            name='expiration_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 2, 2, 16, 46, 16, 678377, tzinfo=utc), null=True),
        ),
    ]
