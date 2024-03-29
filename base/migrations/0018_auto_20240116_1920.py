# Generated by Django 3.2.7 on 2024-01-17 03:20

import django.contrib.auth.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0017_auto_20240103_1706'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Pinbin',
        ),
        migrations.DeleteModel(
            name='Pins',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='firstname',
            new_name='language',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='lastname',
            new_name='nick_name',
        ),
        migrations.RemoveField(
            model_name='user',
            name='birth_date',
        ),
        migrations.RemoveField(
            model_name='user',
            name='dp',
        ),
        migrations.RemoveField(
            model_name='user',
            name='phone',
        ),
        migrations.RemoveField(
            model_name='user',
            name='position',
        ),
        migrations.RemoveField(
            model_name='user',
            name='stronger_foot',
        ),
        migrations.AddField(
            model_name='user',
            name='lightning_address',
            field=models.CharField(max_length=200, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(blank=True, max_length=254, verbose_name='email address'),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(default=django.utils.timezone.now, error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Worldcup',
        ),
    ]
