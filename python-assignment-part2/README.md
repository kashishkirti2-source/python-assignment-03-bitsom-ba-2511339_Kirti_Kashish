# Restaurant Menu & Order Management System - Part 2

In this assignment, I am building a Restaurant Order Management System using Python data structures like dictionaries, lists, and nested dictionaries.

## Task 1 - Explore the Menu
In this task, I printed the restaurant menu grouped by category such as Starters, Mains, and Desserts. I displayed item name, price, and availability status.

I also calculated:
- Total number of items on the menu
- Total number of available items
- The most expensive item on the menu
- Items priced under 150

This task helped me understand how to use nested dictionaries and loops in Python.

## Task 2 - Cart Operations
In this task, I created a cart system using a list of dictionaries. Each cart item stores item name, quantity, and price.

I implemented the following operations:
- Add item to cart
- Remove item from cart
- Update item quantity
- Prevent duplicate items in cart
- Check item availability before adding
- Handle invalid items that do not exist in the menu

I also generated a final order summary which includes subtotal, GST (5%), and total payable amount.

This task helped me understand how to use lists and dictionaries together in a real-world scenario like a restaurant ordering system.

## Task 3 - Inventory Tracker with Deep Copy
In this task, I created a backup of the inventory using deep copy so that the original data remains safe. I modified the inventory and showed that the backup was not affected.

Then I updated the inventory stock based on the items ordered in the cart. If the stock was not enough, I printed a warning and did not allow stock to go below zero.

I also printed reorder alerts for items whose stock was less than or equal to the reorder level.

This task helped me understand deep copy and inventory management logic.
