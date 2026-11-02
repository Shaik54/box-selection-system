from decimal import Decimal
from inventory.models import Box

def calculate_order_totals(order):
    total_weight = Decimal('0')
    total_volume = Decimal('0')

    for item in order.items.select_related('product').all():
        product = item.product
        quantity = item.quantity

        total_weight += product.weight * quantity

        product_volume = product.length * product.width * product.height
        total_volume += product_volume * quantity

    return total_weight, total_volume

def product_fits_box(product, box):
    product_dimensions = [product.length, product.width, product.height]
    box_dimensions = [box.internal_length, box.internal_width, box.internal_height]

    product_dimensions.sort()
    box_dimensions.sort()

    return all(p <= b for p, b in zip(product_dimensions, box_dimensions))

def get_suitable_boxes(order):
    total_weight, total_volume = calculate_order_totals(order)
    suitable_boxes = []

    for box in Box.objects.filter(is_active=True):
        if box.max_weight < total_weight:
            continue

        box_volume = box.internal_length * box.internal_width * box.internal_height

        if box_volume < total_volume:
            continue

        items = order.items.select_related('product').all()

        if all(product_fits_box(item.product, box) for item in items):
            suitable_boxes.append(box)

    return sorted(suitable_boxes, key=lambda box: box.cost)

def recommend_box(order):
    suitable_boxes = get_suitable_boxes(order)

    if not suitable_boxes:
        return None

    return suitable_boxes[0]