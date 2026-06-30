def average(score):
    Sum=sum(score) / len(score)
    return Sum

def letter_grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 80:
        return "B"
    elif marks >= 70:
        return "C"
    elif marks >= 60:
        return "D"
    else:
        return "F"

scores = [85, 90, 78, 92]

avg = average(scores)
grade = letter_grade(avg)

print("Average:", avg)
print("Grade:", grade)