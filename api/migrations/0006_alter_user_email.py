# Generated by Django 4.2.7 on 2023-11-29 06:05

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_alter_user_birth_date_alter_user_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=200, primary_key=True, serialize=False, validators=[django.core.validators.EmailValidator(code='invalied', message='Plase enter valied email')]),
        ),
    ]