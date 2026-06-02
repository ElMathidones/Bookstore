from django.contrib.auth.models import User
from django.test import TestCase

from product.models import Category, Product
from .models import Order
from .serializers import OrderSerializer


class OrderSerializerTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='mathias',
            password='123456'
        )

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

        self.order = Order.objects.create(
            user=self.user,
            product=self.product,
            quantity=2
        )

    def test_order_serializer_fields(self):
        serializer = OrderSerializer(instance=self.order)

        self.assertEqual(
            set(serializer.data.keys()),
            {'id', 'user', 'product', 'quantity', 'created_at'}
        )
