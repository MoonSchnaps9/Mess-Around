list_of_scores = [45, 82, 91, 37, 68, 75, 55, 90, 43, 88]
scores_above_70 = 0
sum_of_scores_above_70 = 0
for score in list_of_scores:
    if score > 70:
        scores_above_70 += 1
        sum_of_scores_above_70 += score
print(f"Total: {sum_of_scores_above_70}")
print(f"Score above 70: {scores_above_70}")