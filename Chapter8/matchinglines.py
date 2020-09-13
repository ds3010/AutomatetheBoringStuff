import re
import os

# Loop to ask the user for a valid folder. If found: save the list of files and folders in a list and break the loop
while True:
    print('Insert an absolute directory path: ')
    path = raw_input()
    try:
        dirlist = os.listdir(path)
        break
    except OSError:
        print('\nDirectory path is not valid, please try again\n')

# Loop to ask for a regular expression
print('Insert a Regular Expression:')
regex = raw_input()
regex2 = regex.capitalize()
regexCom = re.compile(r'^.+?' + regex + '.+?\n', re.MULTILINE)

#For each file in the directory, first make sure it is an actual file and that it ends with .txt
txtRegex = re.compile(r'^.*\.txt$')
print('\nThe following lines within the following files contain the regular expression entered:')
for x in range(len(dirlist)):
    if txtRegex.search(dirlist[x]) != None and os.path.isfile(dirlist[x]):
        fileX = open(dirlist[x], 'r')
        fileXContent = fileX.read()
        print('\nFILE: ' + dirlist[x] + '\n')
        resultList = regexCom.findall(fileXContent)
        for y in range(len(resultList)):
            print('\n' + str(resultList[y]) + '\n')