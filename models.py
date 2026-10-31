from django.db import models


class Service(models.Model):
    service_name = models.CharField(max_length=150)
    description = models.TextField()
    image = models.ImageField(upload_to='services/', blank=True, null=True)
    estimated_duration = models.CharField(max_length=80, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.service_name


class Product(models.Model):
    CATEGORY_CHOICES = [
        ('Accessories', 'Accessories'),
        ('Chargers', 'Chargers'),
        ('Cables', 'Cables'),
        ('Audio', 'Audio'),
        ('Batteries', 'Batteries'),
        ('Protection', 'Protection'),
        ('Cases', 'Cases'),
        ('Components', 'Components'),
    ]

    AVAILABILITY_CHOICES = [
        ('In Stock', 'In Stock'),
        ('Low Stock', 'Low Stock'),
        ('Out of Stock', 'Out of Stock'),
    ]

    product_name = models.CharField(max_length=150)
    category = models.CharField(max_length=30, choices=CATEGORY_CHOICES, default='Accessories')
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    availability = models.CharField(max_length=20, choices=AVAILABILITY_CHOICES, default='In Stock')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.product_name


class ContactInquiry(models.Model):
    customer_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    subject = models.CharField(max_length=150)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.customer_name} - {self.subject}"


class RepairRequest(models.Model):
    REPAIR_CHOICES = [
        ('Screen Replacement', 'Screen Replacement'),
        ('Battery Replacement', 'Battery Replacement'),
        ('Charging Port Repair', 'Charging Port Repair'),
        ('Software Troubleshooting', 'Software Troubleshooting'),
        ('Water Damage Repair', 'Water Damage Repair'),
        ('Speaker and Microphone Repair', 'Speaker and Microphone Repair'),
        ('Camera Repair', 'Camera Repair'),
        ('Hardware Diagnostics', 'Hardware Diagnostics'),
    ]

    PREFERRED_CONTACT_CHOICES = [
        ('Phone', 'Phone'),
        ('Email', 'Email'),
        ('WhatsApp', 'WhatsApp'),
    ]

    STATUS_CHOICES = [
        ('New', 'New'),
        ('In Progress', 'In Progress'),
        ('Awaiting Parts', 'Awaiting Parts'),
        ('Completed', 'Completed'),
    ]

    customer_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    mobile_brand = models.CharField(max_length=100)
    mobile_model = models.CharField(max_length=100)
    repair_category = models.CharField(max_length=50, choices=REPAIR_CHOICES)
    problem_description = models.TextField()
    preferred_contact = models.CharField(max_length=20, choices=PREFERRED_CONTACT_CHOICES, default='Phone')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='New')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.customer_name} - {self.mobile_brand} {self.mobile_model}"
