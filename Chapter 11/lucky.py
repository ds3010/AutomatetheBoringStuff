#! python3
# lucky.py - Opens several Google Search Results

import requests, sys, webbrowser, bs4
print('Googling...')  # display text while downloading the Google page
res = requests.get('http://google.com/search?=' + ' '.join(sys.argv[1:]))
try:
    res.raise_for_status()
except Exception as exc:
    print('There was a problem with your request: %s' % (exc))

# Retrieve top search result links
soup = bs4.BeautifulSoup(res.text, features='lxml')

# Open a browser tab for each result
linkElems = soup.select('.r a')
numOpen = min(5, len(linkElems))
for i in range(numOpen):
    webbrowser.open('http://google.com' + linkElems[i].get('href'))