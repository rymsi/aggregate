# -*- coding: utf-8 -*-
from google.cloud import datastore
import os
from requests import get
from bs4 import BeautifulSoup
import re

        
string = '''Alabama 
Alaska 
Arizona 
Arkansas 
California 
Colorado 
Connecticut 
Delaware 
Florida 
Georgia 
Hawaii 
Idaho 
Illinois Indiana 
Iowa 
Kansas 
Kentucky 
Louisiana 
Maine 
Maryland 
Massachusetts 
Michigan 
Minnesota 
Mississippi 
Missouri 
Montana Nebraska 
Nevada 
New Hampshire 
New Jersey 
New Mexico 
New York 
North Carolina 
North Dakota 
Ohio 
Oklahoma 
Oregon 
Pennsylvania Rhode Island 
South Carolina 
South Dakota 
Tennessee 
Texas 
Utah 
Vermont 
Virginia 
Washington 
West Virginia 
Wisconsin 
Wyoming'''.replace('\n', '').split(' ') 

print(string)
                      
                      
                      
                      
                      
                      


#client = datastore.Client('aggregate-223323')
#query = client.query(kind='senators')
#results = list(query.fetch())
#for result in results:
#    print(result['Propublica'])
##
#result = list(query.fetch())[0]
#
#response = get(result['Ballotpedia'])
#soup = soup = BeautifulSoup(response.content, 'html.parser')
#
#html = soup.find(class_='infobox person')
#print(html)



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



