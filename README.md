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

## Project Architecture

The application is organized into three main parts:

1. **Inventory app** – Manages products and shipping boxes.
2. **Orders app** – Handles customer orders, order items, box recommendation logic, and automated tests.
3. **Config** – Contains the main Django project settings and URL configuration.

### Project Structure

```text
box-selection-system/
│
├── config/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── inventory/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── admin.py
│
├── orders/
│   ├── models.py
│   ├── views.py
│   ├── services.py
│   ├── urls.py
│   ├── admin.py
│   └── tests.py
│
├── templates/
│   ├── products.html
│   └── order_result.html
│
├── manage.py
├── requirements.txt
├── .gitignore
├── README.md
├── AI_USAGE.md
├── TEST_OUTPUT.md
└── docs/
    └── chat_transcript.pdf
```

### Application Flow

```text
Customer
   |
   v
Product Listing Page
   |
   v
Select Products and Quantities
   |
   v
Submit Order
   |
   v
Django Order View
   |
   v
Validate Customer Details and Quantities
   |
   v
Save Order and Order Items
   |
   v
Box Recommendation Service
   |
   v
Calculate Weight and Volume
   |
   v
Check Available Boxes
   |
   v
Select Lowest-Cost Suitable Box
   |
   v
Display Order Result
```

### Main Components

| Component | Responsibility |
|---|---|
| `inventory/models.py` | Product and Box database models |
| `inventory/views.py` | Displays available products |
| `orders/models.py` | Order and OrderItem database models |
| `orders/views.py` | Handles order submission and recommendation API |
| `orders/services.py` | Contains box recommendation logic |
| `orders/tests.py` | Tests recommendation logic and API responses |
| `config/urls.py` | Connects application URL routes |
| `templates/` | Contains HTML pages for product selection and order results |
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
 

- **Django Application Development:** Learned how to structure a Django project using separate applications and understand the responsibilities of models, views, URL configurations, templates, and service files.

- **Database Design and Relationships:** Gained practical experience creating database models for products, boxes, orders, and order items. Understood how foreign-key relationships connect orders with their corresponding products and quantities.

- **Box Recommendation Algorithm:** Learned how to calculate total order weight and volume, compare product dimensions with box dimensions, check weight and volume constraints, and select the lowest-cost suitable box.

- **Input Validation and Error Handling:** Gained experience handling invalid customer details, non-numeric quantities, negative quantities, and orders without selected products.

- **API Development:** Learned how to create Django views that return JSON responses containing recommendation details and appropriate error responses when an order or suitable box is unavailable.

- **AI-Assisted Development:** Learned how to use AI tools during development for understanding requirements, exploring implementation approaches, reviewing code suggestions, and making changes based on the actual project requirements.
