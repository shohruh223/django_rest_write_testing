from django.urls import path, include
from rest_framework.routers import DefaultRouter

from app.views import CategoryModelViewSet, ProductModelViewSet

router = DefaultRouter()
router.register('category', CategoryModelViewSet, basename='category')
router.register('product', ProductModelViewSet, basename='product')


urlpatterns = [
    path('', include(router.urls))
]