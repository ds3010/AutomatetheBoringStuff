import re

# Open and read file into a new variable
madFile = open('madlibs.txt','r')
madContent = madFile.read()

# Let's print the read file to the screen
print('This is the original text:\n')
print(madContent + '\n')

# Create Regex's and put them in a list
regex = re.compile(r'(ADJECTIVE)|(VERB)|(NOUN)|(ADVERB)')

# While Loop where a search on the regex is performed everytime, a word will be entered by the user to replace string found
# If the search comes back empty, break the loop
while True:
        change = regex.search(madContent)
        if change != None:
            for x in range(4):
                if change.group(x) != None:
                    print('Enter ' + change.group(x) + ':')
                    word = raw_input()
                    madContent = regex.sub(word,madContent,1)
                    break
        else:
            break

# Print new text to the Console
print(madContent)

#Export the new content to a new file
newMadFile = open('newMadFile.txt','w')
newMadFile.write(madContent)
