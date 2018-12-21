# -*- coding: utf-8 -*-
from google.cloud import datastore
import os
from requests import get
from bs4 import BeautifulSoup
import re

os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="C:/Users/Junaid/Documents/Aggregate/Scraper/Aggregate-f1762ced81c5.json"


client = datastore.Client('aggregate-223323')
query = client.query(kind='senators')
query.add_filter('Index', '=', 5)


result = list(query.fetch())[0]

response = get(result['Ballotpedia'])
soup = soup = BeautifulSoup(response.content, 'html.parser')

html = soup.find(class_='infobox person')
print(html)













#retval = soup.select('.mw-parser-output > *')
#retlist = ''
#for i in range(len(retval)):
#    if(retval[i].name == 'p'):
#        retlist += '\n\n'+ retval[i].text.strip()
#    if((retval[i].name == 'div') and (retval[i]['class'][0] == 'toc')):
#        break
#
#retlist = re.sub('\[\d*\]', '', retlist.lstrip())
#
#
#print(retlist)                     



