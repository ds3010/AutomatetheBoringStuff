import os

# Ask user for a valid folder to review and change working directory
while True:
    print('Please enter the folder to check: ')
    path = input()
    try:
        os.chdir(path)
        break
    except FileNotFoundError:
        print('This path does not exist please try again')

print('\nFiles bigger than 100MB:')

#Walk inside the directory to look for files bigger than 100MB
for folder, subfolders, files in os.walk(os.getcwd()):
    print('\nFiles inside ' + folder + ':')
    for file in files:
        if os.path.getsize(folder+ '/' + file) >= 104857600:
            print(folder + '/' + file + ': ' + str(os.path.getsize(folder+ '/' + file)))


