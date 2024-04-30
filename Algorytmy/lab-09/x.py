with open("less.txt", "r") as f:
    text = f.read().split(" ")

    words = []

    for word in text:
        if word.isalpha():
            words.append(word)

print(words)
print(len(words))


# find longest word
longest = 0
for word in words:
    if len(word) > longest:
        longest = len(word)

print(longest)


print("a" * 120)
