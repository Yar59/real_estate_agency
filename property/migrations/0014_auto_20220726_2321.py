# Generated by Django 2.2.24 on 2022-07-26 20:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0013_auto_20220726_2253'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='flat',
            name='owner',
        ),
        migrations.RemoveField(
            model_name='flat',
            name='owner_pure_phone',
        ),
        migrations.RemoveField(
            model_name='flat',
            name='owners_phonenumber',
        ),
    ]
