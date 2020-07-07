#! python3
# pw.py - An unsecure password locker program.

PASSWORDS = {'email': 'qwertyuiop123456789',
             'blog': 'asdfghjkl1234567890',
             'luggage': '12345'}

""" The following block of code forces the user to enter an argument equal to the account who needs a password,
If an account wasn't provided (length smaller than 2 characters), the program exits and prints a reminder to include 
the arguments with the command
"""
import sys, pyperclip

if len(sys.argv) < 2:
    print('Usage: Remember to type your username as an argument')
    sys.exit()

account = sys.argv[1]

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Password for ' + account + ' copied to clipboard.')
else:
    print('There is no account named ' + account + '. Do you want to add this account to the password dictionary? (Y/N): ')
    addPwd = raw_input()
    addPwd = addPwd.lower()
    if addPwd == 'y':
        print('\n' + 'Type password for the new account:')
        pwd = raw_input()
        PASSWORDS.setdefault(account, pwd)
        print('\n' + 'Account:'.ljust(15,'.') + ' Password:'.ljust(20))
        for k,v in PASSWORDS.items():
            print(k.ljust(15,'.') + ":" + v.ljust(20))

    else:
        print('Thanks for using this App!')