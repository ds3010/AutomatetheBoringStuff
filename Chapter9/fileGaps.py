import os, re, shutil

#Ask user for a valid folder and change working directory
while True:
    print('Please enter the folder to verify: ')
    path = input()
    try:
        os.chdir(path)
        break
    except FileNotFoundError:
        print('This path does not exist please try again')

os.chdir(path)

#Create a Regular expression that finds files named with a non-numerical word followed by a prefix and then by a file extension
prefixReg = re.compile(r'(\D+)(\d+)\.(\w*)')

#Create a list with the contents inside that folder and create another list removing all directories and 
#files that do not match the regex. Finally, sort the new list
fileList = []
dirList = os.listdir(os.getcwd())
for x in range(len(dirList)):
    if prefixReg.search(dirList[x])!=None and os.path.isfile(dirList[x]):
        fileList.append(dirList[x])
fileList.sort()

#Print List of files before the change
print('BEFORE:')
for x in range(len(fileList)):
    print(fileList[x])
# Check every filename in the new list and make sure the next filename has the same structure
# and its prefix is only one digit higher. If not, then rename the next filename accordingly. 
# The prefix will be stored in group 2 of the already created regex, but notice it will be stored as a string

for x in range(len(fileList)):
    currentFile = prefixReg.search(fileList[x])
    try:
        nextFile = prefixReg.search(fileList[x+1])
    except IndexError:
        break
    if (currentFile.group(1) == nextFile.group(1)) and (int(currentFile.group(2)) != int(nextFile.group(2))-1):
        #First lets add some code that will add zeros to the number so it matches the structure of all the files
        extraZeros = len(currentFile.group(2)) - len(str(int(currentFile.group(2)) + 1))
        if extraZeros <= 0:
            extraZeros = 0
        #Rename the file
        shutil.move('./' + fileList[x+1], './' + nextFile.group(1) + '0'*extraZeros + str(int(currentFile.group(2)) + 1) + '.' + nextFile.group(3))
        #Remember to also change the fileList
        fileList[x+1] = nextFile.group(1) + '0'*extraZeros + str(int(currentFile.group(2)) + 1) + '.' + nextFile.group(3)

print('\nAFTER:')
for x in range(len(fileList)):
    print(fileList[x])
