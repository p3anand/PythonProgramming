'''
Program to calculate and display grades for a score
based on the following grading scale:
A: 90-100
B: 80-89
C: 70-79
D: 60-69
F: 0-59
'''

score = int(input("Enter your score:\n"))
if score>100 or score<0:
    print("Invalid score")
elif 90 <= score <= 100:
    print("Grade = A")
elif 80 <= score <= 89:
    print("Grade = B")
elif 70 <= score <= 79:
    print("Grade = C")
elif 60 <= score <= 69:
    print("Grade = D")
else:
    print("Grade = F")

