score = input("tell me your score:")
score = int(score)
if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
elif score >= 60:
    grade = 'D'        
else:
    grade = 'F'

print (f"Your grade is {grade}") 