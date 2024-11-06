from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from api.serializers import (
    GoodListSerializer,
    GoodSerializer,
    TypeSerializer,
)
from goods.models import Good, Type


class GoodViewSet(viewsets.ModelViewSet):
    '''ViewSet для товара.'''

    queryset = Good.objects.all()

    def get_serializer_class(self):
        if self.action in ('list', 'retrieve'):
            return GoodListSerializer
        return GoodSerializer

    @action(methods=['POST'], url_name='reduce', detail=True)
    def reduce_quantity(self, request, pk=None):
        '''Уменьшение количества товара на складе.'''

        amount = request.data.get('amount')
        if not amount:
            return Response(
                {
                    'error': 'Необходимо указать требуемое количество товара!'
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            good = Good.objects.get(pk=pk)
            if good.quantity >= amount:
                good.quantity -= amount
                good.save()
                return Response(
                    {
                        'message': f'Количество товара {good.name} '
                                   'уменьшено!',
                        'new_quantity': good.quantity
                    },
                    status=status.HTTP_200_OK
                )
            else:
                missing_quantity = amount - good.quantity
                return Response(
                    {
                        'error': 'Недостаточное количество товара '
                                 f'{good.name} на складе! '
                                 f'Не хватает {missing_quantity} шт.'
                    },
                    status=status.HTTP_400_BAD_REQUEST
                )
        except Good.DoesNotExist:
            return Response(
                {
                    'error': f'Товара с id={pk} не существует!'
                },
                status=status.HTTP_404_NOT_FOUND
            )

    @action(methods=['POST'], url_path='add_by_barcode', detail=False)
    def add_good_by_barcode(self, request):
        '''Добавление товара по штрихкоду.'''

        barcode = request.data.get('barcode')
        amount = request.data.get('amount')

        if not (barcode and amount):
            return Response(
                {
                    'error': 'Необходимо указать штрихкод товара и '
                             'его количество!'
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            good = Good.objects.get(barcode=barcode)
            good.quantity += amount
            good.save()
            return Response(
                {
                    'message': f'Количество товара {good.name} увеличено!',
                    'new_quantity': good.quantity
                },
                status=status.HTTP_200_OK
            )
        except Good.DoesNotExist:
            return Response(
                {
                    'error': f'Товара с таким штрихкодом: {barcode} '
                             'не существует! Внесите товар в базу данных.'
                },
                status=status.HTTP_404_NOT_FOUND
            )


class TypeViewSet(viewsets.ModelViewSet):
    '''ViewSet для типа.'''

    queryset = Type.objects.all()
    serializer_class = TypeSerializer
