from datetime import datetime
from decimal import Decimal
from djmoney.models.fields import MoneyField
from djmoney.models.validators import MaxMoneyValidator, MinMoneyValidator

from django.db import models


class Good(models.Model):
    '''Модель для товара.'''

    name = models.CharField(
        verbose_name='Название',
        max_length=150,
        unique=True
    )
    price = MoneyField(
        verbose_name='Цена',
        max_digits=8,
        decimal_places=2,
        default=0,
        default_currency='RUB',
        validators=[
            MinMoneyValidator(
                limit_value=Decimal(0.01),
                message='Цена на товар не может быть отрицательной '
                        'или равняться 0!'
            ),
            MaxMoneyValidator(
                limit_value=Decimal(999999.99),
                message='Цена на товар не может быть больше 999999.99!'
            )
        ]
    )
    quantity = models.PositiveIntegerField(
        verbose_name='Количество',
        default=0
    )
    barcode = models.PositiveBigIntegerField(
        verbose_name='Штрихкод',
        default=0
    )
    update_date = models.DateField(
        verbose_name='Дата обновления',
        default=datetime.now
    )
    type = models.ForeignKey(
        to='Type',
        verbose_name='Тип',
        on_delete=models.CASCADE
    )

    class Meta:
        db_table = 'good'
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ('id', )

    def __str__(self):
        return f'Товар: {self.name} | Количество: {self.quantity}'


class Type(models.Model):
    '''Модель для типа товара.'''

    name = models.CharField(
        verbose_name='Название',
        max_length=150,
        unique=True
    )
    description = models.TextField(
        verbose_name='Описание',
        blank=True,
        null=True
    )

    class Meta:
        db_table = 'good_type'
        verbose_name = 'Тип'
        verbose_name_plural = 'Типы'
        ordering = ('id', )

    def __str__(self):
        return self.name
