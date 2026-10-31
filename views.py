from django.contrib import messages
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render

from .forms import ContactInquiryForm, RepairRequestForm
from .models import Product, RepairRequest, Service


def home(request):
    services = Service.objects.all()[:3]
    products = Product.objects.all()[:4]
    context = {
        'services': services,
        'products': products,
    }
    return render(request, 'repairshop/home.html', context)


def about(request):
    return render(request, 'repairshop/about.html')


def services(request):
    services = Service.objects.all()
    return render(request, 'repairshop/services.html', {'services': services})


def service_detail(request, service_id):
    service = get_object_or_404(Service, id=service_id)
    return render(request, 'repairshop/service_detail.html', {'service': service})


def products(request):
    query = request.GET.get('q', '')
    category = request.GET.get('category', '')
    products = Product.objects.all()

    if category:
        products = products.filter(category=category)
    if query:
        products = products.filter(
            Q(product_name__icontains=query) | Q(description__icontains=query)
        )

    categories = Product.CATEGORY_CHOICES
    return render(
        request,
        'repairshop/products.html',
        {'products': products, 'categories': categories, 'selected_category': category, 'query': query},
    )


def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'repairshop/product_detail.html', {'product': product})


def contact(request):
    if request.method == 'POST':
        form = ContactInquiryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message has been sent successfully. Our team will contact you soon.')
            return redirect('contact')
    else:
        form = ContactInquiryForm()
    return render(request, 'repairshop/contact.html', {'form': form})


def repair_inquiry(request):
    if request.method == 'POST':
        form = RepairRequestForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your repair request has been received. We will get back to you shortly.')
            return redirect('repair_inquiry')
    else:
        form = RepairRequestForm()
    return render(request, 'repairshop/repair_inquiry.html', {'form': form})
