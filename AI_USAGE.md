# AI Usage Documentation

## 1. AI Tool Used

I used ChatGPT during the development of this project to get guidance, understand concepts, solve coding issues, and improve my implementation.

## 2. How I Used AI

I used ChatGPT at different stages of the project.

- **Project Structure:** I discussed how to organize the Django project and decided to keep separate apps for inventory and orders.
- **Models:** I used AI guidance to understand how to create models for products, boxes, orders, and order items.
- **Box Recommendation:** I explored different ways to check product dimensions, total weight, volume, and box cost.
- **Order Handling:** I got help understanding how to handle multiple products and quantities in a single order.
- **Validation:** I discussed how to handle invalid customer details and product quantities.
- **Testing:** I used AI guidance to understand how to write test cases and fix errors during testing.
- **Debugging:** When I faced issues, I shared the relevant code and error messages to understand what was going wrong.

## 3. Prompts Used

The following are examples of prompts used during development. The exported chat transcript contains the actual conversation.

- Explain the requirements and architecture for developing an e-commerce shipping box recommendation system using Django.
- What database models and fields are required to store product details, box dimensions, weight, and cost?
- How can I calculate the total weight and volume of products in an order using Python?
- How can I develop a Python function to check whether a product fits inside a shipping box based on its length, width, and height?
- How can I handle product rotation when checking whether a product fits inside a box?
- How can I recommend the most suitable and cheapest shipping box based on product dimensions, volume, and weight?
- How can I implement the shipping box recommendation algorithm using Django services?
- How can I write automated test cases for input validation, order creation, and box recommendations?
- Review my Django code and suggest improvements, error handling, and best practices.

## 4. AI Suggestions I Used

I reviewed the suggestions from ChatGPT and used some of them in my implementation.

Some examples include:

- Organizing the project into separate Django apps.
- Calculating the total weight and volume of an order.
- Comparing product dimensions with box dimensions.
- Sorting suitable boxes based on their cost.
- Writing test cases for the recommendation functionality.

## 5. Suggestions I Changed or Did Not Use

I did not blindly use every suggestion. I reviewed the proposed solutions and made changes whenever they did not match my requirements.

For example:

- I simplified the project structure to avoid unnecessary complexity.
- I kept the recommendation logic focused on the requirements of the assignment.
- I modified code suggestions to match my existing models and project structure.

## 6. Mistakes and Corrections

During development, I faced issues with order submission, input validation, and testing.

I used ChatGPT to understand these issues, but I also checked the code and tested the changes before keeping them in the project.

I have included the specific mistakes and corrections I encountered during development here:

[Add your actual examples, if applicable.]

## 7. How I Verified the Final Code

I did not rely only on AI-generated code. I checked the application by:

- Running the Django development server.
- Testing order submission through the application.
- Checking invalid quantity inputs.
- Testing the recommendation API using Postman.
- Running automated Django test cases.
- Checking whether the recommended box matched the expected result in different test scenarios.

The final implementation was reviewed and tested before submission.