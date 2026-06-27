alice_scores = [85, 92, 78, 90, 88]
bob_scores = [72, 65, 80, 71, 69]
charlie_scores = [95, 98, 92, 97, 94]
diana_scores = [55, 60, 58, 62, 57]

#So just do it for each student individually — calculate the average for Alice, print it, then Bob, then Charlie, then Diana. Four blocks, same logic repeated.

alice_score_total = 0
number_scores_alice = 0

for ascores in alice_scores:
    alice_score_total += ascores
    number_scores_alice = len(alice_scores)
average_score_alice = alice_score_total / number_scores_alice
print(f"Alice: {average_score_alice}")


b_score_total = 0
number_scores_b = 0

for bscores in bob_scores:
    b_score_total += bscores
    number_scores_b = len(bob_scores)

average_score_b = b_score_total / number_scores_b

print(f"Bob: {average_score_b}")

c_score_total = 0
number_score_c = 0

for cscore in charlie_scores:
    c_score_total += cscore
    number_score_c = len(charlie_scores)

average_score_c = c_score_total / number_score_c

print(F"Charlie: {average_score_c}")

d_score_total = 0
number_scores_d = 0

for dscore in diana_scores:
    d_score_total += dscore
    number_score_d = len(diana_scores)

average_score_d = d_score_total / number_score_d

print(f"Diana: {average_score_d}")