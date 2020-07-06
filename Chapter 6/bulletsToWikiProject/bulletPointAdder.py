#! python3

# bulletPointAdder.py - Adds Wikipedia bullet points to the start
# of each line of text on the clipboard

import pyperclip
text = pyperclip.paste()

# TODO: Separate lines and add stars
textList = text.split('\n')

for x in range(len(textList)):
    textList[x] = '* ' + textList[x]

print('\n###THE FOLLOWING TEXT HAS BEEN COPIED TO YOUR CLIPBOARD:###\n')
for x in textList:
    print(x)

text = '\n'.join(textList)
pyperclip.copy(text)