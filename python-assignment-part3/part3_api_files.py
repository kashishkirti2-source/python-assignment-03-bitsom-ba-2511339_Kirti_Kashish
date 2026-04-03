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
