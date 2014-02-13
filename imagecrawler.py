__author__ = 'neon'
__UserAgent__ = 'Image Downloader Bot by JcGNeon'

from sys import exit
import os
import re
import urllib
from bs4 import BeautifulSoup
import mechanize


def welcome():
    print "Welcome to Image Downloader Bot. To browse Reddit's front page simply leave the subreddit request blank.\n"


def open_url():
    user_subreddit = raw_input('Enter the Subreddit You Wish to Scrape(e.g. /r/aww): ')
    try:
        br = mechanize.Browser()
        response = br.open('http://reddit.com' + user_subreddit)

        # in case the subreddit is NSFW
        if re.search(r'[<title>reddit\.com: over 18\?</title>]', response.read()) is not None:
            br.select_form(nr=2)
            result = br.submit()
            soup = BeautifulSoup(result)
            get_image(soup)
        else:
            soup = BeautifulSoup(response.read())  # scan through the result
            get_image(soup)
    except Exception, e:
        print e
        exit(1)


def get_image(soup):
    for link in soup.find_all('a'):
        new_result = link.get('href')
        some_match = re.search(r'\.jpg|\.png|\.gif', str(new_result))  # check for links with image extensions
        if some_match is not None:
            print str(new_result) + '\n'
            url = str(new_result).split('/')[-1]  # get the filename from the image url
            try:
                if os.path.isfile(url):
                    pass
                else:
                    urllib.urlretrieve(new_result, filename=url, reporthook=None, data=None)  # download the image
            except Exception, e:
                print e


def main():
    open_url()
    print 'Done.'
    exit(0)

if __name__ == '__main__':
    welcome()
    main()
