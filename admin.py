from django.contrib import admin

from .models import ContactInquiry, Product, RepairRequest, Service


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('service_name', 'estimated_duration', 'created_at')
    search_fields = ('service_name', 'description')
    list_filter = ('created_at',)
    ordering = ('-created_at',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'category', 'price', 'availability', 'created_at')
    search_fields = ('product_name', 'description', 'category')
    list_filter = ('category', 'availability', 'created_at')
    ordering = ('-created_at',)


@admin.register(ContactInquiry)
class ContactInquiryAdmin(admin.ModelAdmin):
    list_display = ('customer_name', 'email', 'subject', 'created_at')
    search_fields = ('customer_name', 'email', 'subject', 'message')
    list_filter = ('created_at',)
    ordering = ('-created_at',)


@admin.register(RepairRequest)
class RepairRequestAdmin(admin.ModelAdmin):
    list_display = ('customer_name', 'mobile_brand', 'repair_category', 'status', 'created_at')
    search_fields = ('customer_name', 'email', 'mobile_brand', 'mobile_model', 'problem_description')
    list_filter = ('status', 'repair_category', 'preferred_contact', 'created_at')
    ordering = ('-created_at',)
