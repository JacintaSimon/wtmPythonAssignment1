#Part 1:Python Introduction and Data Types
#Task1: Personal Information
name = "Stephanie "
age = 29
height = '156cm'
is_student = True

print("Name:", name)
print("Age:", age)
print("Height:", height)
print("Student:", is_student)

#Task 2: Identify the Data Types
print(type(name))
print(type(age))
print(type(height))
print(type(is_student))

#Part 2: Lists 
#Task 3: Favorite Foods
foods = ["pizza", "Fried Rice", "Chicken Curry", "pepperpot", "Chocolate Ice Cream"]

print("Original list:", foods)
print("First food:", foods[0])
print("Last food:", foods[-1])

foods.append("curry")
print("After adding curry:", foods)

foods.remove("pepperpot")
print("After removing pepperpot:", foods)

foods[0] = "pasta"
print("After changing pizza to pasta:", foods)
print("Final list:", foods)

#Task 4: Student Scores
scores = [75, 80, 65, 90, 85]
print("Scores:", scores)
print("Highest score:", max(scores))
print("Lowest score:", min(scores))
scores.append(95)
print("Updated list:", scores)

#Part 3: Tuples
#Task 5: Days of the Week
days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")

print("Days:", days)
print("First day:", days[0])
print("Last day:", days[-1])

#Attempt to change one of the values
try:
    days[0] = "Funday"
except TypeError as e:
    print("Error:", e)

"""
Why is a tuple different from a list?
The tuple is immutable, meaning its values cannot be changed after creation, whereas lists are mutable and can be modified. 
This is why attempting to change a value in the tuple results in a TypeError.

"""

"""
Part 4: Sets 
Task #6: Removal of Duplicate Values
Explain why some values disappeared ?
    A Set is a collection of unique values, meaning it automatically removes any duplicate values. 
    In the original list, 1,2, and 3 appeared multiple times. When converted to a set, Python keeps only
    one copy of each value, resulting in the disappearance of the duplicates.
"""
numbers = [1, 2, 3, 4, 2, 5, 3, 6, 1]

specialNumbers = set(numbers)

print("Original list:", numbers)
print("Set:", specialNumbers)

#Task 7: Unique Programming Languages
languages = ["Python", "Java", "Python", "C++", "JavaScript", "Python"]

unique_languages = set(languages)
print("Unique languages:", unique_languages)

unique_languages.add("Django")
print("Updated set:", unique_languages)

"""
Part 5: Dictionaries
Task #8 Student Profile
"""

student = {
    "Name": "Alice",
    "Age": 20,
    "Course": "Computer Science",
    "Level": "Level 1",
    "Skills": ["Python", "Java", "C++"]
}

print("Student:", student)

print("Name:", student["Name"])

student["Email"] = "alice@example.com"

student["Level"] = "Level 3"

del student["Age"]

print("Final dictionary:", student)

"""
FINAL CHALLENGE 
Task 9: Student Management Data
Create a dictionary for 3 students. Each student should have:
    • Name
    • Age
    • Course
    • A list of at least 3 skills
Example structure:
        1. student1:
        a. name: John
        b. age: 22
        c. course: Backend Development,
        d. skills: Python, HTML, Git
    2. student2:
        a. name: Mary
        b. age: 24
        c. course: Data Analysis
        d. skills: Excel, SQL, Python

Your program should print the information for all students.
"""
# Creating a dictionary for each student
student1 = {
    "name": "John",
    "age": 22,
    "course": "Backend Development",
    "skills": ["Python", "HTML", "Git"]
}

student2 = {
    "name": "Mary",
    "age": 24,
    "course": "Data Analysis",
    "skills": ["Excel", "SQL", "Python"]
}

student3 = {
    "name": "David",
    "age": 23,
    "course": "Frontend Development",
    "skills": ["JavaScript", "CSS", "React"]
}

# Storing all students in a list for easy access
students = [student1, student2, student3]

# Printing the information for all students
for index, student in enumerate(students, start=1):
    print(f"Student {index}:")
    print(f"  Name: {student['name']}")
    print(f"  Age: {student['age']}")
    print(f"  Course: {student['course']}")
    print(f"  Skills: {', '.join(student['skills'])}")
    # blank line for spacing between students
    print() 

"""
Assignment: Student Information Manager
Objective
Create a Python program that stores and displays information about a student using different
Python data types and data structures.
Instructions
Create variables containing the following student information:
1. Name – String

2. Age – Integer
3. Height – Float
4. Is currently enrolled – Boolean
Then create the following data structures:
1. List
Create a list containing at least 5 programming languages or subjects the student is interested in.
Example:
Skills: Python, HTML, CSS, JavaScript, SQL
Perform the following:
• Print the first item.
• Add a new item.
• Remove one item.
• Print the updated list.

2. Tuple
Create a tuple containing the student's 3 favorite numbers.
Example:
Favorite numbers = 7, 10, 25
Print the second number.

3. Set
Create a set containing some hobbies. Include at least one duplicate value.
Example:
Hobbies: Reading, Gaming, Football, Reading
• Print the set.
• Explain through the program output what happened to the duplicate value.
• Add a new hobby.

4. Dictionary

Create a dictionary containing all the student's basic information.
Example structure:
name: John
age: 25
height: 1.75,
is enrolled: True
skills: Python, SQL, Excel
favorite numbers: 7, 10, 25
hobbies: Reading, Gaming, Football
Then:
• Print the student's name.
• Print their skills.
• Add a new key called "country".
• Update the student's age.
• Print the complete dictionary.
"""

name = "Sarah"              # String
age = 21                    # Integer
height = 1.65                # Float
is_enrolled = True           # Boolean

print("Name:", name)
print("Age:", age)
print("Height:", height)
print("Is currently enrolled:", is_enrolled)
print()


# 1. List - programming languages/subjects of interest
skills = ["Python", "HTML", "CSS", "JavaScript", "SQL"]

# Print the first item
print("First skill:", skills[0])

# Add a new item
skills.append("Java")

# Remove one item
skills.remove("CSS")

# Print the updated list
print("Updated skills list:", skills)
print()


# 2. Tuple - student's 3 favorite numbers
favorite_numbers = (7, 10, 25)

# Print the second number
print("Second favorite number:", favorite_numbers[1])
print()


# 3. Set - hobbies (includes a duplicate value)
hobbies = {"Reading", "Gaming", "Football", "Reading"}

# Print the set
print("Hobbies:", hobbies)
print("Note: Even though 'Reading' was added twice, it only appears once in")
print("the set, because sets automatically remove duplicate values.")

# Add a new hobby
hobbies.add("Chess")
print("Updated hobbies:", hobbies)
print()


# 4. Dictionary - student's basic information
student = {
    "name": name,
    "age": age,
    "height": height,
    "is_enrolled": is_enrolled,
    "skills": skills,
    "favorite_numbers": favorite_numbers,
    "hobbies": hobbies
}

# Print the student's name
print("Student name:", student["name"])

# Print their skills
print("Student skills:", student["skills"])

# Add a new key called "country"
student["country"] = "Guyana"

# Update the student's age
student["age"] = 22

# Print the complete dictionary
print("Complete student dictionary:", student)



#BONUS CHALLENGE

# Store personal information in variables
name = "Abdurrahman"
age = 25
favorite_language = "Python"

# Store the information in a dictionary
person = {
    "name": name,
    "age": age,
    "favorite_language": favorite_language
}

# Print a formatted greeting using the dictionary
print(f"Hello {person['name']}!")
print(f"You are {person['age']} years old.")
print(f"Your favorite programming language is {person['favorite_language']}.")