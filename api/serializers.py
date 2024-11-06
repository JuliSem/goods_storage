from rest_framework import serializers

from goods.models import Good, Type


class TypeSerializer(serializers.ModelSerializer):
    '''Serializer для типа.'''

    class Meta:
        model = Type
        fields = ('id', 'name', 'description')


class GoodSerializer(serializers.ModelSerializer):
    '''Serializer для создания товара.'''

    class Meta:
        model = Good
        fields = ('id', 'name', 'price', 'price_currency',
                  'quantity', 'barcode', 'update_date', 'type')


class GoodListSerializer(serializers.ModelSerializer):
    '''Serializer для получения товара/ товаров.'''

    type = TypeSerializer(read_only=True)

    class Meta:
        model = Good
        fields = ('id', 'name', 'price', 'price_currency',
                  'quantity', 'barcode', 'update_date', 'type')
