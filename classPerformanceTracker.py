studentCount = int(input("How many student entries do you want to create? "))
student_records = {}

for i in range(studentCount):
    print(f"--- Entry {i + 1} ---")
    name = input("Enter student name: ").strip()
    score = float(input("Enter score (0-100): "))
    student_records[name] = score

print("\n" + "=" * 40) 
"""
instead of putting alot of equals signs, you can use the multiplication operator to repeat a 
string multiple times. In this case, it repeats the "=" 
character 40 times to create a visual separator in the output.

"""
print("EVALUATION RESULTS")
print("=" * 40)

passed = 0
failed = 0

for name, score in student_records.items():
    if score >= 70:
        grade = "A"
        status = "Passed with Distinction"
        passed += 1
    elif score >= 50:
        grade = "B"
        status = "Passed"
        passed += 1
    else:
        grade = "F"
        status = "Needs Improvement"
        failed += 1

    print(f"- {name}: Score {score} | Grade {grade} | {status}")

# Class summary
total_students = len(student_records)
average = sum(student_records.values()) / total_students if total_students else 0.0

print("\n" + "=" * 40)
print("CLASS PERFORMANCE")
print("=" * 40)
print(f"Average Score: {round(average, 2)}")
print(f"Total Passed: {passed}")
print(f"Total Failed: {failed}")