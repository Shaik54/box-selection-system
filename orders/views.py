from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render, redirect
from .models import Order, OrderItem
from inventory.models import Product
from .services import recommend_box
import uuid


def recommend_order_box(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    box = recommend_box(order)

    if not box:
        return JsonResponse({'message': 'No suitable box available'}, status=404)

    return JsonResponse({
        'order_number': order.order_number,
        'recommended_box': box.name,
        'dimensions': {
            'length': float(box.internal_length),
            'width': float(box.internal_width),
            'height': float(box.internal_height)
        },
        'max_weight': float(box.max_weight),
        'cost': float(box.cost)
    })


def place_order(request):
    products = Product.objects.filter(is_active=True)

    if request.method == 'POST':
        customer_name = request.POST.get('customer_name', '').strip()
        selected_items = []

        if not customer_name:
            return render(request, 'products.html', {
                'products': products,
                'error': 'Customer name is required.'
            })

        for product in products:
            try:
                quantity = int(request.POST.get(f'quantity_{product.id}', 0))
            except ValueError:
                return render(request, 'products.html', {
                    'products': products,
                    'error': 'Please enter a valid quantity.'
                })

            if quantity < 0:
                return render(request, 'products.html', {
                    'products': products,
                    'error': 'Quantity cannot be negative.'
                })

            if quantity > 0:
                selected_items.append((product, quantity))

        if not selected_items:
            return render(request, 'products.html', {
                'products': products,
                'error': 'Please select at least one product.'
            })

        order = Order.objects.create(
            order_number=f"ORD-{uuid.uuid4().hex[:8].upper()}",
            customer_name=customer_name
        )

        for product, quantity in selected_items:
            OrderItem.objects.create(order=order, product=product, quantity=quantity)

        box = recommend_box(order)

        return render(request, 'order_result.html', {
            'order': order,
            'box': box
        })

    return redirect('product_list')