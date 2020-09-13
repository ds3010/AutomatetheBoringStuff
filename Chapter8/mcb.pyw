#! python3
# mcb.pyw - Saves and loads pieces of text to the clipboard.
# Usage: py.exe mcb.pyw save <keyword> - Saves clipboard to keyword.
#        py.exe mcb.pyw <keyword> - Loads keyword to clipboard
#        py.exe mcb.pyw list - Loads all keywords to clipboard

import shelve, pyperclip, sys

mcbShelf = shelve.open('mcb')

# Save clipboard content.
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcbShelf[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) == 2:
    # List keywords and load content.
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbShelf.keys())))
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])
# Practice Project 1
elif len(sys.argv) == 3 and sys.argv[1].lower() == 'delete' and sys.argv[2].lower() == 'all':
    newList = list(mcbShelf.keys())
    for x in range(len(newList)):
        del mcbShelf[newList[x]]
elif len(sys.argv) == 3 and sys.argv[1].lower() == 'delete':
    try:
        del mcbShelf[sys.argv[2]]
    except KeyError:
        print('\nThe wildcard entered does not exist.')

mcbShelf.close()