# -------- Task 1: File Read & Write --------

# Product Explorer & Error-Resilient Logger
# In this program, I am learning file handling, API calls, and exception handling.
# In Task 1, I wrote notes to a file, appended new lines, and read the file.
# I also searched for a keyword in the file.

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
    print("Error writing file:", e)


# Append two more lines
try:
    file = open("python_notes.txt", "a", encoding="utf-8")

    file.write("Topic 6: Functions help reuse code.\n")
    file.write("Topic 7: APIs allow communication between applications.\n")

    file.close()
    print("Lines appended successfully.")

except Exception as e:
    print("Error appending file:", e)


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
    print("Error reading file:", e)
