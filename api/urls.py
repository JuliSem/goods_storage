from django.urls import include, path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from rest_framework import routers

from api.views import GoodViewSet, TypeViewSet


router = routers.DefaultRouter()

router.register('goods', GoodViewSet)
router.register('types', TypeViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path(
        'schema/swagger/',
        SpectacularSwaggerView.as_view(url_name='schema'),
        name='swagger'
    ),
]
