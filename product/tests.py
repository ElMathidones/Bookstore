from django.test import TestCase

from .models import Category, Product
from .serializers import CategorySerializer, ProductSerializer


class CategorySerializerTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(
            title='Livros',
            slug='livros',
            description='Categoria de livros',
            active=True
        )

    def test_category_serializer_fields(self):
        serializer = CategorySerializer(instance=self.category)

        self.assertEqual(
            set(serializer.data.keys()),
            {'id', 'title', 'slug', 'description', 'active'}
        )


class ProductSerializerTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(
            title='Livros',
            slug='livros',
            description='Categoria de livros',
            active=True
        )

        self.product = Product.objects.create(
            title='Clean Code',
            description='Livro sobre boas práticas',
            price='99.90',
            active=True
        )

        self.product.categories.add(self.category)

    def test_product_serializer_fields(self):
        serializer = ProductSerializer(instance=self.product)

        self.assertEqual(
            set(serializer.data.keys()),
            {'id', 'title', 'description', 'price', 'active', 'categories'}
        )
