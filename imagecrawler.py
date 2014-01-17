__author__ = 'neon'
from bs4 import BeautifulSoup
from sys import exit
import urllib
import urllib2
import re
import os

def openUrl():
    try:
        result = urllib2.urlopen('http://reddit.com/', data = None)
        soup = BeautifulSoup(result)
        getImage(soup)
    except Exception, e:
        print e
        exit(1)

def getImage(soup):
    for link in soup.find_all('a'):
        new_result = link.get('href')
        someMatch = re.search(r'.jpg|png', str(new_result))
        if(someMatch != None):
            print new_result
            url = str(new_result).split('/')[-1]
            try:
                if os.path.isfile(url):
                    pass
                else:
                    urllib.urlretrieve(new_result, filename = url, reporthook = None, data = None)
            except Exception, e:
                print e

def main():
    openUrl()
    print 'Done.'
    exit(0)

if __name__ == '__main__':
    main()
