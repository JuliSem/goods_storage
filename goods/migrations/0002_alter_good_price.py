# Generated by Django 5.1.2 on 2024-11-05 13:40

import django.core.validators
import djmoney.models.fields
from decimal import Decimal
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='good',
            name='price',
            field=djmoney.models.fields.MoneyField(decimal_places=2, default=Decimal('0'), default_currency='RUB', max_digits=8, validators=[django.core.validators.MinValueValidator(Decimal('0.01'), message='Цена на товар не может быть отрицательной!')], verbose_name='Цена'),
        ),
    ]
