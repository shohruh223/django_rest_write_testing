from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from app.models import Category, Product
from app.serializers import CategoryModelSerializer, ProductModelSerializer


class CategoryModelViewSet(ModelViewSet):
    queryset = Category.objects.all()
    permission_classes = (IsAuthenticated, )
    serializer_class = CategoryModelSerializer


class ProductModelViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductModelSerializer