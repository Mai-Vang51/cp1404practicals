"""
CP1404/CP5632 Practical
Word Occurrences
Estimate: 1 hour
Actual: 1 hour 56 minutes
"""

word_to_count = {}

text = input("Text: ")
words = text.split()
for word in words:
    try:
        word_to_count[word] += 1
    except KeyError:
        word_to_count[word] = 1

longest_word_length = max((len(word) for word in words))

for word, count in sorted(word_to_count.items()):
    print(f"{word:{longest_word_length}} : {count}")

