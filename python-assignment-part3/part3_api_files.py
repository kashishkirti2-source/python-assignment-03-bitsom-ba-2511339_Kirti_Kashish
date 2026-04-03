# Product Explorer & Error-Resilient Logger
# In this program, I am learning file handling and exception handling.
# I am writing notes to a file, reading them, and handling errors using try-except.
# If any error occurs, it will be saved in error_log.txt.

# function to log errors
def log_error(error_message):
    file = open("error_log.txt", "a")
    file.write(error_message + "\n")
    file.close()


# -------- Task 1: File Read & Write --------

# Part A — Write to file
try:
    file = open("python_notes.txt", "w", encoding="utf-8")

    file.write("Topic 1: Variables store data. Python is dynamically typed.\n")
    file.write("Topic 2: Lists are ordered and mutable.\n")
    file.write("Topic 3: Dictionaries store key-value pairs.\n")
    file.write("Topic 4: Loops automate repetitive tasks.\n")
    file.write("Topic 5: Exception handling prevents crashes.\n")

    file.close()
    print("File written successfully.")

except Exception as e:
    print("Error writing file.")
    log_error("Write Error: " + str(e))


# Append two more lines
try:
    file = open("python_notes.txt", "a", encoding="utf-8")

    file.write("Topic 6: Functions help reuse code.\n")
    file.write("Topic 7: APIs allow communication between applications.\n")

    file.close()
    print("Lines appended successfully.")

except Exception as e:
    print("Error appending file.")
    log_error("Append Error: " + str(e))


# Part B — Read file
try:
    file = open("python_notes.txt", "r", encoding="utf-8")

    lines = file.readlines()
    file.close()

    print("\nReading File:")
    count = 0

    for line in lines:
        count += 1
        print(f"{count}. {line.strip()}")

    print("\nTotal number of lines:", count)

    # keyword search
    keyword = input("\nEnter a keyword to search: ").lower()
    found = False

    for line in lines:
        if keyword in line.lower():
            print(line.strip())
            found = True

    if not found:
        print("No lines found with that keyword.")

except Exception as e:
    print("Error reading file.")
    log_error("Read Error: " + str(e))
    
    
    # -------- Task 2: API Integration --------

import requests

print("\nFetching products from API...\n")

# Step 1 — Fetch and display products
try:
    url = "https://dummyjson.com/products?limit=20"
    response = requests.get(url)
    data = response.json()

    products = data["products"]

    print("ID  | Title                          | Category      | Price    | Rating")
    print("----|--------------------------------|---------------|----------|-------")

    for p in products:
        print(f"{p['id']:<3} | {p['title']:<30} | {p['category']:<13} | ${p['price']:<8} | {p['rating']}")

except Exception as e:
    print("Error fetching products:", e)


# Step 2 — Filter rating >= 4.5 and sort by price (descending)
print("\nFiltered Products (Rating >= 4.5, Sorted by Price):\n")

filtered = []

for p in products:
    if p["rating"] >= 4.5:
        filtered.append(p)

# sort by price descending
filtered.sort(key=lambda x: x["price"], reverse=True)

for p in filtered:
    print(p["title"], "- $", p["price"], "- Rating:", p["rating"])


# Step 3 — Search by category (laptops)
print("\nLaptop Products:\n")

try:
    laptop_url = "https://dummyjson.com/products/category/laptops"
    response = requests.get(laptop_url)
    laptop_data = response.json()

    for item in laptop_data["products"]:
        print(item["title"], "- $", item["price"])

except Exception as e:
    print("Error fetching laptops:", e)


# Step 4 — POST request (simulate adding product)
print("\nSending POST request...\n")

try:
    post_url = "https://dummyjson.com/products/add"

    new_product = {
        "title": "My Custom Product",
        "price": 999,
        "category": "electronics",
        "description": "A product I created via API"
    }

    response = requests.post(post_url, json=new_product)
    result = response.json()

    print("Response from server:")
    print(result)

except Exception as e:
    print("Error sending POST request:", e)
    
    
    # -------- Task 3: Exception Handling --------

# Part A — safe divide function
def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: Cannot divide by zero"
    except TypeError:
        return "Error: Invalid input types"

print("\nSafe Divide Tests:")
print(safe_divide(10, 2))
print(safe_divide(10, 0))
print(safe_divide("ten", 2))


# Part B — safe file reader
def read_file_safe(filename):
    try:
        file = open(filename, "r")
        content = file.read()
        file.close()
        return content
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    finally:
        print("File operation attempt complete.")

print("\nReading python_notes.txt:")
print(read_file_safe("python_notes.txt"))

print("\nReading ghost_file.txt:")
read_file_safe("ghost_file.txt")