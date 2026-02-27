# Stage 3: Student Grade Calculator
# Task: Calculate student grade based on marks in 3 subjects.

# Input: Student name, 3 subject marks (0-100)

# Calculate:

# Total marks
# Percentage = (total/300) * 100

# Grade Logic:

# A: >= 75%
# B: >= 60%
# C: >= 40%
# F: < 40%

a,b,c,d=(input("Enter student name and three subject marks(0-100) as comma separated values (eg: Maria Thomas,80,70,90)").split(","))

def grade():
    if Percentage >= 75:
        print("A Grade")
    if Percentage >=60 and Percentage <75:
        print("B Grade")
    if Percentage >=40 and Percentage <60:
        print("C Grade")
    if Percentage <40:
        print("F Grade")

print("Student Name:", a)
print(f"Total:{int(b)+int(c)+int(d)}/300")
Percentage=((int(b)+int(c)+int(d))/300)*100
print("Percentage:",Percentage)
grade()
