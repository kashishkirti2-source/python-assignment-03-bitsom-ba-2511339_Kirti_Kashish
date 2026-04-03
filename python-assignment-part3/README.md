## Task 1 - File Read & Write
In this task, I wrote Python notes to a file called python_notes.txt using write mode. Then I appended two more lines using append mode. After that, I read the file and printed each line with numbering. I also counted the total number of lines and implemented a keyword search feature.

I also implemented exception handling using try-except blocks so that the program does not crash if any error occurs.

This task helped me understand file handling and error handling in Python.


## Task 2 - API Integration

In this task, I used the requests library to fetch product data from a public API.
I fetched 20 products and displayed them in a formatted table.
Then I filtered products with rating greater than or equal to 4.5 and sorted them by price in descending order.
I fetched laptop products using category search and printed their names and prices.
I also sent a POST request to simulate adding a new product and printed the server response.
I used try-except blocks to handle possible errors while making API requests.


## Task 3 - Exception Handling

In this task, I implemented exception handling in different situations.

First, I created a function safe_divide(a, b) that performs division and handles errors like division by zero and invalid input types using try-except.

Second, I created a function read_file_safe(filename) that reads a file safely. If the file does not exist, it shows an error message instead of crashing the program. I also used a finally block to print a message after every file operation attempt.

I also added exception handling in my API calls to handle connection errors, timeout errors, and other unexpected errors so that the program does not crash if the API request fails.