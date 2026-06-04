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


from rest_framework import status
from rest_framework.test import APIClient

class ProductViewSetTest(TestCase):
    def setUp(self):
        self.client = APIClient()

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

    def test_list_products(self):
        response = self.client.get('/api/products/')

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_create_product(self):
        response = self.client.post(
            '/api/products/',
            {
                'title': 'Python Avançado',
                'description': 'Livro de Python',
                'price': '59.90',
                'active': True,
                'categories': [self.category.id]
            },
            format='json'
        )

        self.assertEqual(response.status_code, 201)

