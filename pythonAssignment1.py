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