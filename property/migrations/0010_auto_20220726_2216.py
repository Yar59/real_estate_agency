# Generated by Django 2.2.24 on 2022-07-26 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0009_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='owner',
            name='pure_number',
            field=models.CharField(max_length=20, null=True, verbose_name='Нормализованный номер владельца'),
        ),
    ]
