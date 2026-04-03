# Task 1: Cleaning and parsing student data
# Here we are given raw data, so first we will clean it and convert into proper format

raw_students = [
    {"name": "  ayesha SHARMA  ", "roll": "101", "marks_str": "88, 72, 95, 60, 78"},
    {"name": "ROHIT verma",       "roll": "102", "marks_str": "55, 68, 49, 72, 61"},
    {"name": "  Priya Nair  ",    "roll": "103", "marks_str": "91, 85, 88, 94, 79"},
    {"name": "karan MEHTA",       "roll": "104", "marks_str": "40, 55, 38, 62, 50"},
    {"name": " Sneha pillai ",    "roll": "105", "marks_str": "75, 80, 70, 68, 85"},
]

# Loop through each student to clean their data
for student in raw_students:

    # Remove extra spaces from name and convert to proper title format
    name = student["name"].strip().title()

    # Convert roll number from string to integer
    roll = int(student["roll"])

    # Convert marks from string to list
    marks_string = student["marks_str"].split(",")
    marks = []
    for m in marks_string:
        marks.append(int(m.strip()))

    # Check if name is valid (only alphabets in each word)
    valid_name = True
    for word in name.split():
        if not word.isalpha():
            valid_name = False

    # Print whether name is valid or not
    if valid_name:
        print(name, "- Valid name")
    else:
        print(name, "- Invalid name")

    # Print student profile
    print("================================")
    print(f"Student : {name}")
    print(f"Roll No : {roll}")
    print(f"Marks   : {marks}")
    print("================================")


# Now print name in upper and lower case for roll number 103
for student in raw_students:
    if int(student["roll"]) == 103:
        name = student["name"].strip().title()
        print("\nName formats for Roll 103:")
        print(name.upper())
        print(name.lower())