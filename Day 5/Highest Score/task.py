student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]
print(range(1, 10))
#sum using function
total_sum = sum(student_scores)
print(total_sum)
#sum manally
sum=0
for score in student_scores:
    sum+=score
print(sum)
#max using function
print(max(student_scores))
#max manually my own logic
maximum_score = student_scores[0]
for max_score in student_scores:
    if max_score > maximum_score:
        maximum_score = max_score

print(maximum_score)


