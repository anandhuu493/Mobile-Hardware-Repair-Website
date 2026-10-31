from django.test import TestCase
from django.urls import reverse

from .models import ContactInquiry, Product, Service


class RepairShopViewsTest(TestCase):
    def setUp(self):
        self.service = Service.objects.create(
            service_name='Screen Replacement',
            description='Replace cracked and damaged phone screens with quality display assemblies.',
            image='services/screen-repair.svg',
            estimated_duration='45-60 minutes',
        )
        self.product = Product.objects.create(
            product_name='USB-C Charger',
            category='Chargers',
            description='Fast and safe charging adapter for modern smartphones.',
            price='29.99',
            image='products/quick-charger.svg',
            availability='In Stock',
        )

    def test_home_page_renders(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Expert Mobile Repair & Hardware Solutions')
        self.assertContains(response, self.service.service_name)
        self.assertContains(response, self.product.product_name)

    def test_contact_form_submits_and_stores_inquiry(self):
        response = self.client.post(
            reverse('contact'),
            {
                'customer_name': 'John Smith',
                'email': 'john@example.com',
                'phone': '+1234567890',
                'subject': 'Repair question',
                'message': 'I need help with a screen replacement for my device.',
            },
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(ContactInquiry.objects.count(), 1)
        self.assertEqual(ContactInquiry.objects.first().customer_name, 'John Smith')
