# AI-Assisted Box Selection System

## Project Overview

The AI-Assisted Box Selection System is a Django-based application that recommends a suitable shipping box for an order based on product dimensions, total weight, box capacity, and box cost.

The system checks available boxes and recommends the lowest-cost box that satisfies the order requirements.

## Features

- Manage products and their dimensions and weight.
- Manage shipping boxes and their internal dimensions, maximum weight capacity, and cost.
- Display available products through an HTML page.
- Place orders containing multiple products and quantities.
- Validate customer details and product quantities.
- Calculate total order weight and volume.
- Check whether products fit inside available boxes.
- Recommend the lowest-cost suitable box.
- Return recommendation details through a JSON API.
- Handle cases where no suitable box is available.

## Technologies Used

- Python
- Django
- MySQL
- HTML
- Git and GitHub
- Postman

## Project Structure

```text
box_selection_system/
├── config/
├── inventory/
├── orders/
│   ├── models.py
│   ├── services.py
│   ├── views.py
│   ├── urls.py
│   └── tests.py
├── templates/
│   ├── products.html
│   └── order_result.html
├── manage.py
├── requirements.txt
└── .gitignore
```

## Box Recommendation Approach

The recommendation process follows these steps:

1. Retrieve the products and quantities in an order.
2. Calculate the total order weight and volume.
3. Retrieve active boxes from the database.
4. Check whether each box has sufficient weight capacity.
5. Compare product dimensions with the internal dimensions of each box, allowing different orientations.
6. Check whether the total product volume fits within the box volume.
7. Sort suitable boxes by cost.
8. Recommend the lowest-cost suitable box.

If no suitable box is available, the system returns a message indicating that no suitable box was found.

## Installation and Setup

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd box_selection_system
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure the database

Create a MySQL database and configure the database connection in Django settings.

Keep database credentials and secret keys out of GitHub.

### 4. Apply migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Run the development server

```bash
python manage.py runserver
```

### 6. Open the application

```text
http://127.0.0.1:8000/
```

## Testing

Run the automated tests using:

```bash
python manage.py test orders
```

The tests cover box recommendation logic, product fit checks, weight capacity, and recommendation API responses.

## Limitations

The current recommendation algorithm uses individual product dimension checks, aggregate order volume, and total weight. It does not perform full three-dimensional packing or verify the physical arrangement of multiple products inside a box.

## What I Learned
 
- Django models and database relationships.
- Handling orders with multiple products.
- Implementing box recommendation logic.
- Writing and running unit tests.
- Debugging and validating application functionality.
- Using AI tools during development and reviewing their output.
