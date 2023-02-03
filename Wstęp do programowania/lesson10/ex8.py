with open('test.txt', 'r') as fh:
    text = fh.read()

# swap every 'tak' to 'nie'
text = text.replace('tak', 'nie')

with open('test2.txt', 'w') as fh:
    fh.write(text)

