word_list = ["cat", "elephant", "sun", "butterfly", "dog", "strawberry", "hat", "programming", "sky", "mountain"]

minimum_word_length_user = int(input("minimum word length?\n"))
total_word_matched = 0

for word in word_list:
    if len(word) > minimum_word_length_user:
        total_word_matched += 1
        print(word)

print(f"{total_word_matched} words found")