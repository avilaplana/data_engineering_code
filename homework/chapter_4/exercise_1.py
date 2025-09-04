# 1. Customer Order Analysis: Write python code that processes a list of customer orders
# to calculate the total revenue and find top 3 the most frequent customer.
# We have a list of orders, where each order is a dictionary with keys: customer_id, product,
# quantity, and price.
# revenue = quantity * price
# frequency of customer is defined as the number of orders
# orders = [
# {"customer_id": "C001", "product": "laptop", "quantity": 2, "price": 1200.00},
# {"customer_id": "C002", "product": "mouse", "quantity": 1, "price": 25.99},
# {"customer_id": "C001", "product": "keyboard", "quantity": 1, "price": 89.50},
# {"customer_id": "C003", "product": "monitor", "quantity": 1, "price": 299.99},
# {"customer_id": "C002", "product": "laptop", "quantity": 1, "price": 1200.00},
# {"customer_id": "C004", "product": "headphones", "quantity": 3, "price": 79.99},
# {"customer_id": "C001", "product": "webcam", "quantity": 1, "price": 45.00},
# {"customer_id": "C003", "product": "mouse", "quantity": 2, "price": 25.99},
# {"customer_id": "C002", "product": "speaker", "quantity": 1, "price": 150.00},
# {"customer_id": "C005", "product": "tablet", "quantity": 1, "price": 399.99}
# ]

from collections import Counter

orders = [
    {"customer_id": "C001", "product": "laptop", "quantity": 2, "price": 1200.00},
    {"customer_id": "C002", "product": "mouse", "quantity": 1, "price": 25.99},
    {"customer_id": "C001", "product": "keyboard", "quantity": 1, "price": 89.50},
    {"customer_id": "C003", "product": "monitor", "quantity": 1, "price": 299.99},
    {"customer_id": "C002", "product": "laptop", "quantity": 1, "price": 1200.00},
    {"customer_id": "C004", "product": "headphones", "quantity": 3, "price": 79.99},
    {"customer_id": "C001", "product": "webcam", "quantity": 1, "price": 45.00},
    {"customer_id": "C003", "product": "mouse", "quantity": 2, "price": 25.99},
    {"customer_id": "C002", "product": "speaker", "quantity": 1, "price": 150.00},
    {"customer_id": "C005", "product": "tablet", "quantity": 1, "price": 399.99}
]

total_individual_revenues = [order["quantity"] * order["price"] for order in orders]
print(total_individual_revenues)
total_revenue = round(sum(total_individual_revenues),2)
print(total_revenue)

customer_counts = Counter(order["customer_id"] for order in orders)
print(customer_counts)

print(customer_counts.most_common(3))

