#Check a character exists in a number or not?

num = 12345
char = '3'

if char in str(num):
    print(f"{char} exists in {num}")

else:
    print(f"{char} does not exist in {num}")




'''Question: You are tasked with developing a Python program that takes the marks
obtained by a student in the SSC examination and calculates the corresponding
grade, grade point, and percentage range according to the SSC grading system in
Bangladesh.'''


# input the marks obtained by a student.
marks = float(input("Enter the marks obtained by the student: "))

# Calculate the percentage achieved by the student.
percentage = (marks / 100) * 100

# calculating grade, grade point, and percentage range according to percentage achieved by the student
if percentage >= 80:
    grade = "A+"
    grade_point = 5.0
    percentage_range = "80% - 100%"
elif percentage >= 70:
    grade = "A"
    grade_point = 4.0
    percentage_range = "70% - 79%"
elif percentage >= 60:
    grade = "A-"
    grade_point = 3.5
    percentage_range = "60% - 69%"
elif percentage >= 50:
    grade = "B"
    grade_point = 3.0
    percentage_range = "50% - 59%"
elif percentage >= 40:
    grade = "C"
    grade_point = 2.0
    percentage_range = "40% - 49%"
elif percentage >= 33:
    grade = "D"
    grade_point = 1.0
    percentage_range = "33% - 39%"
else:
    grade = "F"
    grade_point = 0.0
    percentage_range = "Below 33%"

# Display results
print("Grade:", grade)
print("Grade Point:", grade_point)
print("Percentage Range:", percentage_range)