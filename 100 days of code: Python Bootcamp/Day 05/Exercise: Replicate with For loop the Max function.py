#Replicate the max function with a For Loop
student_scores = [78, 45, 92, 61, 88, 34, 97, 55, 73, 81, 156, 45]

print(max(student_scores))

#Attempt 1
highest_grade = student_scores[0]
for score in student_scores:
    if score > highest_grade:
        highest_grade = score
print(highest_grade)