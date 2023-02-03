word, pattern, iff = 'rabarbar', 'afdgfdb', 'nie'
for i in range(0, len(word)-len(pattern)): iff = 'nie' if (word[i:i+len(pattern)] != pattern and iff == 'nie') else 'tak'
print(iff)