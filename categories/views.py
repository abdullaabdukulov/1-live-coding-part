from rest_framework import generics
from .models import Category
from .serializers import CategorySerializer
from .pagination import CategoryListPagination


class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = CategoryListPagination