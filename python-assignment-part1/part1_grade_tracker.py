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


# Task 2 - Marks Analysis Using Loops & Conditionals

student_name = "Ayesha Sharma"
subjects = ["Math", "Physics", "CS", "English", "Chemistry"]
marks = [88, 72, 95, 60, 78]

print("Student Name:", student_name)
print("-----------------------------")

# printing subject, marks and grade
for i in range(len(subjects)):
    if marks[i] >= 90:
        grade = "A+"
    elif marks[i] >= 80:
        grade = "A"
    elif marks[i] >= 70:
        grade = "B"
    elif marks[i] >= 60:
        grade = "C"
    else:
        grade = "F"

    print(subjects[i], ":", marks[i], "Grade:", grade)

# total and average
total = 0
for m in marks:
    total = total + m

avg = total / len(marks)

print("-----------------------------")
print("Total Marks =", total)
print("Average Marks =", round(avg, 2))

# highest and lowest
high = marks[0]
low = marks[0]
high_sub = subjects[0]
low_sub = subjects[0]

for i in range(len(marks)):
    if marks[i] > high:
        high = marks[i]
        high_sub = subjects[i]
    if marks[i] < low:
        low = marks[i]
        low_sub = subjects[i]

print("Highest Scoring Subject:", high_sub, "-", high)
print("Lowest Scoring Subject:", low_sub, "-", low)

# while loop for adding new subjects
count = 0

while True:
    sub = input("Enter new subject name (or type done to stop): ")

    if sub.lower() == "done":
        break

    mark_input = input("Enter marks for " + sub + ": ")

    if mark_input.isdigit():
        mark_input = int(mark_input)

        if mark_input >= 0 and mark_input <= 100:
            subjects.append(sub)
            marks.append(mark_input)
            count = count + 1
        else:
            print("Marks should be between 0 and 100")

    else:
        print("Invalid input, please enter numbers only")

print("-----------------------------")
print("New subjects added:", count)

new_total = 0
for m in marks:
    new_total = new_total + m

new_avg = new_total / len(marks)
print("Updated Average:", round(new_avg, 2))
