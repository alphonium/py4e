try:
    score = float(input("Enter score: "))
except:
    score = -1

if score >= 0 and score <= 1:
    if score >= 0.9:
        grade = 'A'
    elif score >= 0.8:
        grade = 'B'
    elif score >= 0.7:
        grade = 'C'
    elif score >= 0.6:
        grade = 'D'
    else:
        grade = 'F'
else:
    grade = "Bad score"

print(grade)