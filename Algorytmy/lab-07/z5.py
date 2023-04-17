def file_managment():
    file = open("3700.txt", "r+")
    return [arg.replace("\n", "") for arg in file]


def strongHash(word):
    hashing = 1
    for i in range(1, len(word)):
        hashing = hashing * (111 * ord(word[i - 1]) + ord(word[i]))
    return hashing


def weakHash(word):
    hashing = 0
    for i in range(len(word)):
        hashing = hashing + ord(word[i])
    return hashing


def emptyList(length):
    return [[] for _ in range(length)]


listWithString = file_managment()
print(
    "\n-------------------------------------------------------- 17 --------------------------------------------------------------------\n"
)

# DEFAULT HASH
print(":::::::: Default Hash :::::::::::\n")
array = emptyList(34)
for i in range(17):
    array[(hash(listWithString[i]) % 34)].append(listWithString[i])
maxi = 0
empty = 0
lenNotEmpty = 0
countNotEmpty = 0
for i in array:
    if len(i) > maxi:
        maxi = len(i)
    if len(i) == 0:
        empty = empty + 1
    else:
        lenNotEmpty = lenNotEmpty + len(i)
        countNotEmpty = countNotEmpty + 1

print("Maximum length of the longest element with 1024 elements is equal: ", maxi)
print("Count of empty elements: ", empty)
print(
    "Average of length of not empty elements: ",
    round(lenNotEmpty / countNotEmpty, 3),
    end="\n\n",
)

# STRONG HASH
print(":::::::: Self strong Hash :::::::::::\n")
array = emptyList(34)
for i in range(17):
    array[(strongHash(listWithString[i]) % 34)].append(listWithString[i])
maxi = 0
empty = 0
lenNotEmpty = 0
countNotEmpty = 0
for i in array:
    if len(i) > maxi:
        maxi = len(i)
    if len(i) == 0:
        empty = empty + 1
    else:
        lenNotEmpty = lenNotEmpty + len(i)
        countNotEmpty = countNotEmpty + 1

print("Maximum length of the longest element with 1024 elements is equal: ", maxi)
print("Count of empty elements: ", empty)
print(
    "Average of length of not empty elements: ",
    round(lenNotEmpty / countNotEmpty, 3),
    end="\n\n",
)

# WEAK HASH
print(":::::::: Self weak Hash :::::::::::\n")
array = emptyList(34)
for i in range(17):
    array[(weakHash(listWithString[i]) % 34)].append(listWithString[i])
maxi = 0
empty = 0
lenNotEmpty = 0
countNotEmpty = 0
for i in array:
    if len(i) > maxi:
        maxi = len(i)
    if len(i) == 0:
        empty = empty + 1
    else:
        lenNotEmpty = lenNotEmpty + len(i)
        countNotEmpty = countNotEmpty + 1

print("Maximum length of the longest element with 1024 elements is equal: ", maxi)
print("Count of empty elements: ", empty)
print(
    "Average of length of not empty elements: ",
    round(lenNotEmpty / countNotEmpty, 3),
    end="\n\n",
)

print(
    "\n-------------------------------------------------------- 1031 --------------------------------------------------------------------\n"
)

# DEFAULT HASH
print(":::::::: Default Hash :::::::::::\n")
array = emptyList(2062)
for i in range(1031):
    array[(hash(listWithString[i]) % 2062)].append(listWithString[i])
maxi = 0
empty = 0
lenNotEmpty = 0
countNotEmpty = 0
for i in array:
    if len(i) > maxi:
        maxi = len(i)
    if len(i) == 0:
        empty = empty + 1
    else:
        lenNotEmpty = lenNotEmpty + len(i)
        countNotEmpty = countNotEmpty + 1

print("Maximum length of the longest element with 1024 elements is equal: ", maxi)
print("Count of empty elements: ", empty)
print(
    "Average of length of not empty elements: ",
    round(lenNotEmpty / countNotEmpty, 3),
    end="\n\n",
)

# STRONG HASH
print(":::::::: Self strong Hash :::::::::::\n")
array = emptyList(2062)
for i in range(1031):
    array[(strongHash(listWithString[i]) % 2062)].append(listWithString[i])
maxi = 0
empty = 0
lenNotEmpty = 0
countNotEmpty = 0
for i in array:
    if len(i) > maxi:
        maxi = len(i)
    if len(i) == 0:
        empty = empty + 1
    else:
        lenNotEmpty = lenNotEmpty + len(i)
        countNotEmpty = countNotEmpty + 1

print("Maximum length of the longest element with 1024 elements is equal: ", maxi)
print("Count of empty elements: ", empty)
print(
    "Average of length of not empty elements: ",
    round(lenNotEmpty / countNotEmpty, 3),
    end="\n\n",
)

# WEAK HASH
print(":::::::: Self weak Hash :::::::::::\n")
array = emptyList(2062)
for i in range(1031):
    array[(weakHash(listWithString[i]) % 2062)].append(listWithString[i])
maxi = 0
empty = 0
lenNotEmpty = 0
countNotEmpty = 0
for i in array:
    if len(i) > maxi:
        maxi = len(i)
    if len(i) == 0:
        empty = empty + 1
    else:
        lenNotEmpty = lenNotEmpty + len(i)
        countNotEmpty = countNotEmpty + 1

print("Maximum length of the longest element with 1024 elements is equal: ", maxi)
print("Count of empty elements: ", empty)
print(
    "Average of length of not empty elements: ",
    round(lenNotEmpty / countNotEmpty, 3),
    end="\n\n",
)


print(
    "\n-------------------------------------------------------- 1024 --------------------------------------------------------------------\n"
)

# DEFAULT HASH
print(":::::::: Default Hash :::::::::::\n")
array = emptyList(2048)
for i in range(1024):
    array[(hash(listWithString[i]) % 2048)].append(listWithString[i])
maxi = 0
empty = 0
lenNotEmpty = 0
countNotEmpty = 0
for i in array:
    if len(i) > maxi:
        maxi = len(i)
    if len(i) == 0:
        empty = empty + 1
    else:
        lenNotEmpty = lenNotEmpty + len(i)
        countNotEmpty = countNotEmpty + 1

print("Maximum length of the longest element with 1024 elements is equal: ", maxi)
print("Count of empty elements: ", empty)
print(
    "Average of length of not empty elements: ",
    round(lenNotEmpty / countNotEmpty, 3),
    end="\n\n",
)


# STRONG HASH
print(":::::::: Strong Hash :::::::::::\n")
array = emptyList(2048)
for i in range(1024):
    array[(strongHash(listWithString[i]) % 2048)].append(listWithString[i])
maxi = 0
empty = 0
lenNotEmpty = 0
countNotEmpty = 0
for i in array:
    if len(i) > maxi:
        maxi = len(i)
    if len(i) == 0:
        empty = empty + 1
    else:
        lenNotEmpty = lenNotEmpty + len(i)
        countNotEmpty = countNotEmpty + 1

print("Maximum length of the longest element with 1024 elements is equal: ", maxi)
print("Count of empty elements: ", empty)
print(
    "Average of length of not empty elements: ",
    round(lenNotEmpty / countNotEmpty, 3),
    end="\n\n",
)


# WEAK HASH
print(":::::::: Weak Hash :::::::::::\n")
array = emptyList(2048)
for i in range(1024):
    array[(weakHash(listWithString[i]) % 2048)].append(listWithString[i])
maxi = 0
empty = 0
lenNotEmpty = 0
countNotEmpty = 0
for i in array:
    if len(i) > maxi:
        maxi = len(i)
    if len(i) == 0:
        empty = empty + 1
    else:
        lenNotEmpty = lenNotEmpty + len(i)
        countNotEmpty = countNotEmpty + 1

print("Maximum length of the longest element with 1024 elements is equal: ", maxi)
print("Count of empty elements: ", empty)
print(
    "Average of length of not empty elements: ",
    round(lenNotEmpty / countNotEmpty, 3),
    end="\n\n",
)
