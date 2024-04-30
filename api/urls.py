from django.urls import path
from .views import VendorAPIView, VendorDetailAPIView, PurchaseOrderListCreateAPIView, PurchaseOrderDetailAPIView, VendorPerformanceAPIView

urlpatterns = [
    path('vendors/', VendorAPIView.as_view(), name='vendor-list-create'),
    path('vendors/<int:vendor_id>/', VendorDetailAPIView.as_view(), name='vendor-detail'),
    path('purchase_orders/', PurchaseOrderListCreateAPIView.as_view(), name='purchase-order-list-create'),
    path('purchase_orders/<int:po_id>/', PurchaseOrderDetailAPIView.as_view(), name='purchase-order-detail'),
    path('vendors/<int:vendor_id>/performance/', VendorPerformanceAPIView.as_view(), name='vendor-performance')
]
