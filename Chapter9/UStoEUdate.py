import shutil, os, re

#Create Regex
datePattern = re.compile(r"""^(.*?) # all text before date format
    ((0|1)?\d)-                     # Month
    ((0|1|2|3)?\d)-                 # Day
    ((19|20)\d{2})                  # Year
    (.*?)$                          # Text after date
    """, re.VERBOSE)

#Call os.listdir() to find all the files in the working directory
fileList = os.listdir()

#Loop over each filename, using the regex to check whether it has a date
for file in range(len(fileList)):
    dateSearch = datePattern.search(fileList[file])
    #If it has a date, rename the file with shutil.move()
    if dateSearch != None:
        shutil.move(fileList[file], dateSearch.group(1) + dateSearch.group(4) + '-' + dateSearch.group(2) + '-' + 
                    dateSearch.group(6) + dateSearch.group(8))