# Known Issues: can't browse NSFW subreddits due to getting stuck on the 'Are you 18?' page.

__author__ = 'neon'
__UserAgent__ = 'Image Downloader Bot by JcGNeon'
from bs4 import BeautifulSoup
from sys import exit
import urllib
import urllib2
import re
import os

def welcome():
    print 'Welcome to Image Downloader Bot. To browse Reddit\'s front page simply leave the subreddit request blank.\n'

def openUrl():
    userSubreddit = raw_input('Enter the Subreddit You Wish to Scrape(e.g. /r/aww): ')
    try:
        result = urllib2.urlopen('http://reddit.com' + userSubreddit + '/?count=' + str(25), data = None)
        soup = BeautifulSoup(result) # scan through the result
        getImage(soup)
    except Exception, e:
        print e
        exit(1)

def getImage(soup):
    for link in soup.find_all('a'):
        new_result = link.get('href')
        someMatch = re.search(r'.jpg|.png|.gif', str(new_result)) # check for links with image extensions
        if(someMatch != None):
            print new_result
            print '\n'
            url = str(new_result).split('/')[-1] # get the filename from the image url
            try:
                if os.path.isfile(url):
                    pass
                else:
                    urllib.urlretrieve(new_result, filename = url, reporthook = None, data = None) # download the image
            except Exception, e:
                print e

def main():
    openUrl()
    print 'Done.'
    exit(0)

if __name__ == '__main__':
    welcome()
    main()
