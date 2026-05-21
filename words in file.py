file = open("note.txt", "r")

data = file.read()

file.close()

words = data.split()

vowels = "aeiouAEIOU"

total_words = len(words)

total_vowels = 0

print("Total words =", total_words)

print("Word-wise vowel count:\n")

for word in words:

    count = 0

    for char in word:

        if char in vowels:

            count += 1
            total_vowels += 1

    print(word, "->", count, "vowels")

print("\nFINAL COUNT")

print("Total vowels =", total_vowels)
