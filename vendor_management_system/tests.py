from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from vendors.models import Vendor
from purchase_orders.models import PurchaseOrder, HistoricalPerformance
from datetime import datetime
from django.utils import timezone

class VendorModelTestCase(TestCase):
    def setUp(self):
        self.vendor = Vendor.objects.create(
            name='Test Vendor',
            contact_details='test@example.com',
            address='123 Test St',
            vendor_code='TEST123'
        )

    def test_vendor_creation(self):
        """Test if a vendor is created successfully."""
        self.assertEqual(Vendor.objects.count(), 1)
        self.assertEqual(self.vendor.name, 'Test Vendor')
        self.assertEqual(self.vendor.contact_details, 'test@example.com')
        self.assertEqual(self.vendor.address, '123 Test St')
        self.assertEqual(self.vendor.vendor_code, 'TEST123')

    def test_vendor_string_representation(self):
        """Test if the string representation of a vendor is correct."""
        self.assertEqual(str(self.vendor), 'Test Vendor')


class PurchaseOrderModelTestCase(TestCase):
    def setUp(self):
        self.vendor = Vendor.objects.create(
            name='Test Vendor',
            contact_details='test@example.com',
            address='123 Test St',
            vendor_code='TEST123'
        )
        self.purchase_order = PurchaseOrder.objects.create(
            po_number='PO123',
            vendor=self.vendor,
            order_date=timezone.make_aware(datetime(2024, 4, 30, 12, 0, 0)),
            delivery_date=timezone.make_aware(datetime(2024, 5, 10, 12, 0, 0)),
            items=[{'name': 'Item A', 'quantity': 5}],
            quantity=5,
            status='pending'
        )

    def test_purchase_order_creation(self):
        """Test if a purchase order is created successfully."""
        self.assertEqual(PurchaseOrder.objects.count(), 1)
        self.assertEqual(self.purchase_order.po_number, 'PO123')
        self.assertEqual(self.purchase_order.vendor, self.vendor)
        self.assertEqual(self.purchase_order.order_date, timezone.make_aware(datetime(2024, 4, 30, 12, 0, 0)))
        self.assertEqual(self.purchase_order.delivery_date, timezone.make_aware(datetime(2024, 5, 10, 12, 0, 0)))
        self.assertEqual(self.purchase_order.quantity, 5)
        self.assertEqual(self.purchase_order.status, 'pending')

    def test_purchase_order_string_representation(self):
        """Test if the string representation of a purchase order is correct."""
        self.assertEqual(str(self.purchase_order), 'PO123')


class VendorPerformanceAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.vendor = Vendor.objects.create(
            name='Test Vendor',
            contact_details='test@example.com',
            address='123 Test St',
            vendor_code='TEST123'
        )

    def test_retrieve_vendor_performance_api(self):
        """Test if a vendor's performance metrics can be retrieved via API."""
        response = self.client.get(reverse('vendor-performance', args=[self.vendor.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Add assertions for performance metrics
