# Test Execution Report

## Test Command

```bash
python manage.py test orders
```

## Test Results

The automated tests were executed using Django's test framework.

## Terminal Output


PS C:\Users\ahmed\OneDrive\Desktop\box_selection_system> python manage.py test orders
Found 8 test(s).
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
........
----------------------------------------------------------------------
Ran 8 tests in 0.340s

OK
Destroying test database for alias 'default'...
PS C:\Users\ahmed\OneDrive\Desktop\box_selection_system> 

## Test Cases Covered

1. Checking whether a product fits inside a box.
2. Checking whether a product does not fit inside a box.
3. Verifying that the cheapest suitable box is recommended.
4. Checking when no suitable box is available.
5. Checking insufficient box weight capacity.
6. Testing the recommendation API with a valid order.
7. Testing the recommendation API when no suitable box is available.
8. Testing the recommendation API with an invalid order.