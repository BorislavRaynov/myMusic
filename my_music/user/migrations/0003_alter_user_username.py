# Generated by Django 4.2.2 on 2023-06-20 14:41

import django.core.validators
from django.db import migrations, models
import my_music.user.models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_alter_user_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=15, validators=[my_music.user.models.check_valid_username, django.core.validators.MinLengthValidator(2)]),
        ),
    ]