#!/usr/bin/env python
import os, sys, time

from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import pyperclip

parser = argparse.ArgumentParser(usage='%(prog)s [-h] [-p PLAYLISTURL] [-d DESTINATION]')
parser.add_argument('-p', '--playlisturl', help='url of the playlist to be downloaded', default=default_url, metavar='')
parser.add_argument('-d', '--destination', help='path of directory to save videos to', default=os.path.curdir, metavar='')
args = parser.parse_args()

playlist_url = "https://www.youtube.com/playlist?list=PLrAXtmErZgOeiKm4sgNOknGvNjby9efdf"
#req = Request(playlist_url)
r = urlopen(playlist_url)
soup = BeautifulSoup(r, 'lxml')
print(soup.title.string.replace(' - YouTube', ''))
page_elements = [x.decode('utf-8') for x in urlopen(playlist_url).readlines()]
video_elements = [el for el in page_elements if 'pl-video-title-link' in el]  # Filter out unnecessary lines
video_urls = [v.split('href="',1)[1].split('" ',1)[0] for v in video_elements]

print('********************************************')
print(str(len(video_urls)))


