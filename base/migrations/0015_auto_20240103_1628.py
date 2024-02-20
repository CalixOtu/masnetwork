# Generated by Django 3.2.7 on 2024-01-04 00:28

import datetime
import django.core.validators
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0014_auto_20240103_0137'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pins',
            name='expiration_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 2, 3, 0, 28, 36, 179668, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='dp',
            field=models.ImageField(default='avatar.svg', null=True, upload_to='', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png']), django.core.validators.MaxValueValidator(102400)]),
        ),
    ]
