#! python3
# pw.py - An unsecure password locker program.

PASSWORDS = {'email': 'qwertyuiop123456789',
             'blog': 'asdfghjkl1234567890',
             'luggage': '12345'}

""" The following block of code forces the user to enter an argument equal to the account who needs a password,
If an account wasn't provided (length smaller than 2 characters), the program exits and prints a reminder to include 
the arguments with the command
"""
import sys

if len(sys.argv) < 2:
    print('Usage: python pw.py [account] - copy account password')
    sys.exit()

account = sys.argv[1]