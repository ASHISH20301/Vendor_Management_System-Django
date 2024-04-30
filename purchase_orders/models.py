from django.db import models
from vendors.models import Vendor
from django.db.models.signals import post_save
from django.dispatch import receiver

class PurchaseOrder(models.Model):
    po_number = models.CharField(max_length=100, unique=True)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    order_date = models.DateTimeField()
    delivery_date = models.DateTimeField()
    items = models.JSONField()
    quantity = models.IntegerField()
    status = models.CharField(max_length=20, default='pending')
    quality_rating = models.FloatField(null=True, blank=True)
    issue_date = models.DateTimeField(auto_now_add=True)
    acknowledgment_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.po_number



class HistoricalPerformance(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    date = models.DateTimeField()
    on_time_delivery_rate = models.FloatField()
    quality_rating_avg = models.FloatField()
    average_response_time = models.FloatField()
    fulfillment_rate = models.FloatField()

    def __str__(self):
        return f'{self.vendor.name} - {self.date}'



@receiver(post_save, sender=PurchaseOrder)
def calculate_on_time_delivery_rate(sender, instance, **kwargs):
    if instance.status == 'completed':
        vendor = instance.vendor
        completed_orders_count = PurchaseOrder.objects.filter(vendor=vendor, status='completed').count()
        on_time_delivery_count = PurchaseOrder.objects.filter(vendor=vendor, status='completed', delivery_date__lte=instance.delivery_date).count()
        on_time_delivery_rate = (on_time_delivery_count / completed_orders_count) * 100 if completed_orders_count != 0 else 0
        vendor.on_time_delivery_rate = on_time_delivery_rate
        vendor.save()



@receiver(post_save, sender=PurchaseOrder)
def update_quality_rating_average(sender, instance, **kwargs):
    if instance.status == 'completed' and instance.quality_rating is not None:
        vendor = instance.vendor
        completed_orders = PurchaseOrder.objects.filter(vendor=vendor, status='completed', quality_rating__isnull=False)
        quality_rating_avg = completed_orders.aggregate(avg_quality_rating=models.Avg('quality_rating'))['avg_quality_rating']
        vendor.quality_rating_avg = quality_rating_avg
        vendor.save()

@receiver(post_save, sender=PurchaseOrder)
def calculate_average_response_time(sender, instance, **kwargs):
    if instance.acknowledgment_date:
        vendor = instance.vendor
        response_times = PurchaseOrder.objects.filter(vendor=vendor, acknowledgment_date__isnull=False).annotate(response_time=models.ExpressionWrapper(models.F('acknowledgment_date') - models.F('issue_date'), output_field=models.DurationField()))
        average_response_time = response_times.aggregate(avg_response_time=models.Avg('response_time'))['avg_response_time']
        vendor.average_response_time = average_response_time.total_seconds() / 3600  # Convert to hours
        vendor.save()

@receiver(post_save, sender=PurchaseOrder)
def calculate_fulfillment_rate(sender, instance, **kwargs):
    vendor = instance.vendor
    total_orders = PurchaseOrder.objects.filter(vendor=vendor).count()
    successful_orders = PurchaseOrder.objects.filter(vendor=vendor, status='completed', issue_date__isnull=False).count()
    fulfillment_rate = (successful_orders / total_orders) * 100 if total_orders != 0 else 0
    vendor.fulfillment_rate = fulfillment_rate
    vendor.save()
