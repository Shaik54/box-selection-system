from django.test import TestCase
from inventory.models import Product, Box
from orders.models import Order, OrderItem
from orders.services import product_fits_box, recommend_box
from orders.services import get_suitable_boxes
from django.urls import reverse

class BoxRecommendationTests(TestCase):

    def setUp(self):
        self.product = Product.objects.create(
            name="Laptop",
            length=30,
            width=20,
            height=5,
            weight=2
        )

        self.box = Box.objects.create(
            name="Medium",
            internal_length=35,
            internal_width=25,
            internal_height=10,
            max_weight=5,
            cost=35
        )

    def test_product_fits_box(self):
        result = product_fits_box(self.product, self.box)

        self.assertTrue(result)

    def test_product_does_not_fit_box(self):
        self.box.internal_length = 25
        self.box.internal_width = 15
        self.box.internal_height = 10
        self.box.save()

        result = product_fits_box(self.product, self.box)

        self.assertFalse(result)

    def test_recommend_cheapest_box(self):
        expensive_box = Box.objects.create(
            name="Large",
            internal_length=40,
            internal_width=30,
            internal_height=20,
            max_weight=10,
            cost=60
        )

        order = Order.objects.create(
            order_number="ORD001",
            customer_name="Test Customer"
        )

        OrderItem.objects.create(
            order=order,
            product=self.product,
            quantity=1
        )

        recommended_box = recommend_box(order)

        self.assertEqual(recommended_box, self.box)

    def test_no_suitable_box_available(self):
        self.box.max_weight = 1
        self.box.save()

        order = Order.objects.create(
        order_number="ORD002",
        customer_name="Test Customer"
        )

        OrderItem.objects.create(
        order=order,
        product=self.product,
        quantity=1
        )

        recommended_box = recommend_box(order)

        self.assertIsNone(recommended_box)

    def test_box_rejected_for_insufficient_weight(self):
        order = Order.objects.create(
        order_number="ORD003",
        customer_name="Test Customer"
        )

        OrderItem.objects.create(
        order=order,
        product=self.product,
        quantity=1
        )

        self.box.max_weight = 1
        self.box.save()

        suitable_boxes = get_suitable_boxes(order)

        self.assertNotIn(self.box, suitable_boxes)

    def test_recommendation_api_success(self):
        order = Order.objects.create(order_number="ORD004", customer_name="Test Customer")
        OrderItem.objects.create(order=order, product=self.product, quantity=1)

        response = self.client.get(reverse('recommend_order_box', args=[order.id]))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['recommended_box'], 'Medium')
        self.assertEqual(response.json()['cost'], 35.0)



    def test_recommendation_api_no_suitable_box(self):
        order = Order.objects.create(order_number="ORD005", customer_name="Test Customer")
        OrderItem.objects.create(order=order, product=self.product, quantity=1)

        self.box.max_weight = 1
        self.box.save()

        response = self.client.get(reverse('recommend_order_box', args=[order.id]))

        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json()['message'], 'No suitable box available')


    def test_recommendation_api_invalid_order(self):
        response = self.client.get(reverse('recommend_order_box', args=[9999]))

        self.assertEqual(response.status_code, 404)
    
