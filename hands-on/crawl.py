#!/usr/bin/env python3
from bs4 import Beautifulsoup
from urllib.request import urlopen
with urlopen('https://en.wikipedia.org/wiki/Main_Page') as response:
	soup= Beautifulsoup(response, 'html.parser')
	for anchor in soup.find_all('a'):
		print(anchor.get('href','/'))
