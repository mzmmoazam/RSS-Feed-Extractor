import os
import requests,logging,sys
from bs4 import BeautifulSoup
'''

This will print all the RSS feeds of a url
you need to enter the filename containing all the urls for which the rss feeds are to be found.

python ExtractRSS.py text.txt

'''
def get_rss_feed(website_url):
    if website_url is None:
        print("URL should not be null")
    else:
        source_code = requests.get(website_url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text, "html.parser")
        # print(soup)
        if not soup.find("link",{"type" : "application/rss+xml"}):
            # create logger
            logger=logging.basicConfig(filename='norss.log',format='%(asctime)s - %(name)s - %(message)s')
            logger = logging.getLogger('URL with on RSS feed : ')
            logger.setLevel(logging.DEBUG)

            # create console handler and set level to debug
            ch = logging.StreamHandler()
            ch.setLevel(logging.DEBUG)

            # add ch to logger
            logger.addHandler(ch)

            # 'application' code
            logger.info(website_url)
        else:
            print ("RSS feed for " + website_url + "is -->\n")
            for link in soup.find_all("link", {"type" : "application/rss+xml"}):
                href = link.get('href')
                print(  str(href))
            print('\n')

if __name__ == '__main__':
    filename,urls='',[]
    if len(sys.argv)>1:
        filename=sys.argv[1]
    else:
        print ("please enter filename as command line argument")
        # exit(0)

        # for development purpose
        filename=' C:/Users/Moazam/Desktop/test.txt'
    try:
        print (os.path.join(os.path.abspath(os.path.basename(filename)),os.path.basename(filename)))
        with open(os.path.join(os.path.abspath(os.path.basename(filename)))) as f:
            urls=f.readlines()
    except IOError as i:
            print(" Enter Path of file  with forward slashes.(e.g C:/Users/Moazam/Desktop/test.txt)")
    urls=[i.strip()for i in urls]
    for i in urls:
        get_rss_feed(i)
